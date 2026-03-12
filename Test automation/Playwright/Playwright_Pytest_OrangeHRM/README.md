# QA Portfolio - Test Automation (OrangeHRM)

Playwright-based test automation framework targeting the [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/).

## About This Project

This is a **portfolio showcase** demonstrating test automation patterns and architecture I developed during professional work on a workforce management application (under NDA).

This project was generated with AI assistance (Cursor). The architecture, patterns, and design decisions (POM, component structure, API client pattern, session singleton) are my own.

**What's demonstrated here:**
- Page Object Model with multi-level inheritance
- Reusable UI components (Datepicker, Table)
- Data-driven test scenarios using Python dataclasses
- Pytest fixture architecture with session- and function-scoped test data
- Fluent/chainable method API for readable test flows
- Automatic screenshot and Playwright trace capture on failure
- Structured logging throughout all page objects

## Prerequisites

- Python 3.12+
- Chrome/Chromium Browser

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/anna-pohle/QA_Portfolio.git
cd "QA_Portfolio/Test automation/Playwright/Playwright_Pytest_OrangeHRM"
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt

# Install browser:
playwright install chromium
```

### 4. Configure credentials

```bash
cp tests/testdata/login_data.yaml.example tests/testdata/login_data.yaml
```

For the OrangeHRM demo, the default credentials are public: `Admin` / `admin123`.

## Running Tests

```bash
# All tests
pytest tests/

# Single test file
pytest tests/test_login.py -v

# Smoke tests only
pytest -m smoke

# Specific feature module
pytest -m feature_pim
pytest -m feature_leave
pytest -m feature_login
```

### Screenshots & Traces

On test failure, the following are automatically saved:
- **Screenshots**: `test-results/screenshots/` (full-page `.png`)
- **Playwright Traces**: `test-results/traces/` (interactive `.zip` files)

Traces can be analyzed locally:
```bash
playwright show-trace test-results/traces/<filename>.zip
```

## Test User & Fixtures

The framework provides two strategies for test data:

### Overview

```
+---------------------------------------------------------------------------+
|                           TEST SESSION                                    |
+---------------------------------------------------------------------------+
|                                                                           |
|  +---------+ +---------+ +---------+ +---------+                          |
|  | Test 1  | | Test 2  | | Test 3  | | Test 4  |                          |
|  | Login   | | Login   | | Leave   | | Leave   |                          |
|  | (valid) | | (empty) | | (1 day) | | (multi) |                          |
|  +----+----+ +----+----+ +----+----+ +----+----+                          |
|       |           |           |           |                               |
|       v           v           v           v                               |
|  +---------+ +---------+ +-------------------------------+                |
|  | test_   | | (no     | |      session_employee         |                |
|  | employee| | fixture)| |   (session-scoped)            |                |
|  |(function| |         | |                               |                |
|  +---------+ +---------+ |  +-----+ +-----+ +-----+     |                |
|  | Created |             | | Day | | Day | | Day |     |                |
|  | Used    |             | |  1  | |  2  | |  3  |     |                |
|  | Deleted |             | +-----+ +-----+ +-----+     |                |
|  +---------+             |                               |                |
|                          |  One employee, many days      |                |
|                          +-------------------------------+                |
|                                         |                                 |
|                                         v                                 |
|                                 Session end:                              |
|                                 Employee is deleted                       |
+---------------------------------------------------------------------------+
```

### Function-Scoped Fixtures (Standard)

For each test a **new employee is created and deleted afterwards**.

```python
def test_search_employee(browser_page, admin_credentials, test_employee):
    # test_employee is a fresh Employee only for this test
    employee_list = (
        LoginPage(browser_page)
        .login_with_credentials(*admin_credentials)
        .click_pim()
        .search_by_employee_name(test_employee.full_name)
    )
```

**Available fixtures:**
| Fixture | Scope | Purpose |
|---------|-------|---------|
| `test_employee` | function | Fresh employee per test, deleted after |
| `session_employee` | session | Persistent employee for shared state |
| `admin_credentials` | session | Admin login tuple (username, password) |
| `browser_page` | function | Playwright Page with tracing enabled |

### Session-Scoped Fixture (Singleton)

A **persistent employee for the entire test session**. Ideal when multiple tests
operate on the same employee (e.g. assigning leave on different dates).

```python
from tests.testdata.singleton import EmployeeSession
from framework.utils.date_utils import DateUtils

def test_assign_leave(browser_page, admin_credentials, session_employee):
    session = EmployeeSession()
    days_ahead = session.get_next_future_day()  # 1, 2, 3, ...
    leave_date = DateUtils.get_date_x_days_from_now(days_ahead)

    LoginPage(browser_page)
        .login_with_credentials(*admin_credentials)
        .click_leave()
        .click_assign_leave()
        .assign_leave(
            employee_name=session_employee.full_name,
            leave_type="CAN - Vacation",
            from_date=leave_date,
            to_date=leave_date,
        )
```

**When to use the Singleton?**
- Tests that assign leave (each test needs its own date)
- Performance-critical test suites (employee creation saves ~2 sec per test)
- Tests that build on each other

**Day counter:**
| Method | Start value | Example |
|--------|-------------|---------|
| `get_next_future_day()` | 1 (tomorrow) | 1 -> 2 -> 3 -> ... |

## Pytest Markers

Tests can be categorized with markers:

```bash
# Smoke tests
pytest -m smoke

# Feature-specific
pytest -m feature_login
pytest -m feature_pim
pytest -m feature_leave

# Combine
pytest -m "smoke and feature_login"
```

**Available markers:**
- `@pytest.mark.smoke` - Quick, critical tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.feature_login` - Login module
- `@pytest.mark.feature_pim` - PIM / Employee Management module
- `@pytest.mark.feature_leave` - Leave Management module

## Project Structure

```
Playwright_Pytest_OrangeHRM/
├── framework/
│   ├── dataclasses/               # Data models
│   │   ├── data_object_employee.py    # Employee dataclass
│   │   ├── employee_config.py         # Employee presets for creation
│   │   ├── leave_scenarios.py         # Test scenarios with expected results
│   │   └── leave_types.py             # LeaveType & LeaveStatus enums
│   ├── pages/                     # Page Object Model (E2E)
│   │   ├── abstract_pages/            # Base classes
│   │   │   ├── base_page.py               # Navigation, element interaction
│   │   │   └── base_page_w_sidebar.py     # Sidebar nav, top bar, logout
│   │   ├── components/                # Reusable UI components
│   │   │   ├── datepicker.py              # OrangeHRM calendar component
│   │   │   └── table_component.py         # Record table (rows, search, count)
│   │   ├── login_module/
│   │   ├── dashboard_module/
│   │   ├── pim_module/                # Employee management
│   │   └── leave_module/              # Leave management
│   ├── utils/                     # Helpers (date_utils, string_utils)
│   └── system_config.py           # URLs, timeouts, browser config
├── tests/
│   ├── testdata/                  # Test configuration
│   │   └── singleton.py               # EmployeeSession for persistent data
│   ├── conftest.py                # Pytest fixtures (browser, employees)
│   ├── test_login.py              # Login tests
│   ├── test_employee.py           # PIM / Employee Management tests
│   └── test_leave.py              # Leave Management tests
├── pytest.ini
└── requirements.txt
```

## Architecture Patterns

### POM Inheritance

```
BasePage (navigate, click, fill, is_visible, wait_for_element)
  └── BasePageWithSidebar (sidebar nav, top bar, logout)
        ├── DashboardPage
        ├── EmployeeListPage (search, filter, table)
        ├── AddEmployeePage (employee creation form)
        ├── LeaveListPage (leave records, sub-navigation)
        └── AssignLeavePage (leave assignment form)
```

### Component Extraction

Reusable UI components are extracted from page objects:
- `DatepickerComponent` — calendar navigation and date selection
- `TableComponent` — row access, counting, loading state

### Fluent API

Methods return `self` to enable chaining:
```python
LoginPage(browser_page)
    .login_with_credentials(username, password)
    .click_pim()
    .click_add_employee()
    .fill_employee_form("John", "Doe")
    .click_save()
```

### Retry Mechanism

Flaky tests are automatically retried once (configured via `--reruns=1`).
The delay between retries is 2 seconds.
In `test-results/junit.xml`, reruns are marked as separate `<testcase>` entries.

## Important

**The following files contain sensitive data and are in `.gitignore`:**
- `tests/testdata/login_data.yaml` (credentials)

These files must **never** be committed to the repository!

## Notes

- The OrangeHRM demo site resets periodically — test data is temporary
- Tests use unique names (UUID suffix) to avoid conflicts with other users
