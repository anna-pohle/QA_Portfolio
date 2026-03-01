# QA Portfolio - Test Automation (OrangeHRM)

Playwright-based test automation framework targeting the [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/).

## About This Project

This is a **portfolio showcase** demonstrating test automation patterns and architecture I developed during professional work on a workforce management application (under NDA).

The architecture, design patterns, and testing strategies shown here are adapted from that real project to target a publicly accessible demo application. This allows me to demonstrate my approach without exposing proprietary code.

**What's demonstrated here:**
- Page Object Model with multi-level inheritance
- Reusable UI components (Datepicker, Table)
- Data-driven test scenarios using Python dataclasses
- Pytest fixture architecture with session- and function-scoped test data
- Fluent/chainable method API for readable test flows
- Automatic screenshot and Playwright trace capture on failure
- Structured logging throughout all page objects

## Tech Stack

- **Language:** Python 3.12+
- **Test Framework:** pytest
- **Browser Automation:** Playwright
- **Pattern:** Page Object Model (POM)

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd qa_portfolio_sanitized
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

## Pytest Markers

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

## Project Structure

```
qa_portfolio_sanitized/
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

## Notes

- The OrangeHRM demo site resets periodically — test data is temporary
- Tests use unique names (UUID suffix) to avoid conflicts with other users
- The retry mechanism (`--reruns=1`) handles occasional demo site instability
