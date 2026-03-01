import logging
import uuid
import yaml
from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from framework.dataclasses.data_object_employee import Employee
from framework.dataclasses.employee_config import EmployeePreset, QA_PRESET
from framework.system_config import BROWSER_CONFIG, DEFAULT_TIMEOUT
from tests.testdata.singleton import EmployeeSession

logger = logging.getLogger(__name__)


# Pytest hooks for test logging
@pytest.hookimpl()
def pytest_runtest_logstart(nodeid, location):
    """Logs the start of a test."""
    logger.info(f"Starting test: {nodeid}")


@pytest.hookimpl()
def pytest_runtest_logfinish(nodeid, location):
    """Logs the end of a test."""
    logger.info(f"Finished test: {nodeid}")


# Pytest hook for screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot on failure."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# Load admin credentials from YAML
def load_admin_credentials():
    """Loads admin credentials from login_data.yaml.

    Returns:
        Tuple of (username, password).
    """
    conftest_dir = Path(__file__).parent  # tests/
    login_data_path = conftest_dir / "testdata" / "login_data.yaml"

    with open(login_data_path, 'r') as f:
        data = yaml.safe_load(f)

    admin = data['admin_user']
    return admin['username'], admin['password']


# Playwright object
@pytest.fixture(scope="session")
def playwright():
    """Provides Playwright object for session-wide fixtures."""
    with sync_playwright() as p:
        yield p


# Page object
@pytest.fixture
def browser_page(playwright, request):
    """
    Opens browser and provides a Page object.

    Includes:
    - Central default timeout (from system_config.py)
    - Playwright tracing for debugging on failures
    - Automatic screenshots on test errors
    """
    browser = playwright.chromium.launch(**BROWSER_CONFIG)
    context = browser.new_context()

    # Start tracing: Records clicks, network requests, DOM snapshots.
    # On failure the trace file is saved and can be analyzed interactively
    # with "playwright show-trace <file>.zip".
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)

    yield page

    # Save screenshot and trace on failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        screenshot_dir = Path("test-results/screenshots")
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = screenshot_dir / f"{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        logger.info(f"Screenshot saved: {screenshot_path}")

        trace_dir = Path("test-results/traces")
        trace_dir.mkdir(parents=True, exist_ok=True)
        trace_path = trace_dir / f"{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        context.tracing.stop(path=str(trace_path))
        logger.info(f"Trace saved: {trace_path}")
    else:
        context.tracing.stop()

    context.close()
    browser.close()


# Admin credentials fixture
@pytest.fixture(scope="session")
def admin_credentials():
    """
    Provides admin credentials as (username, password) tuple.
    Scope: session (loaded once).
    """
    username, password = load_admin_credentials()
    logger.info(f"Admin credentials loaded for: {username}")
    return username, password


# =============================================================================
# TEST EMPLOYEE FIXTURES
# =============================================================================
# Sorted by scope:
#   1. session_employee - session-scoped, shared across tests
#   2. test_employee - function-scoped, fresh employee per test
#
# Function-scoped fixtures = fresh employee per test
# Session-scoped fixtures = same employee for all tests
# =============================================================================


@pytest.fixture(scope="session")
def session_employee(playwright, admin_credentials):
    """
    Session-persistent employee for tests that share state.

    This employee is created ONCE per test session and reused
    across all tests. Ideal for:
    - Leave assignment tests (need a known employee)
    - Tests that check data created by previous tests

    The employee is tracked via the EmployeeSession singleton.

    Usage:
        def test_something(browser_page, session_employee):
            login_page.login_with_credentials(...)
            assign_leave_page.select_employee(session_employee.full_name)
    """
    session = EmployeeSession()

    # Only create if not already existing
    if session.primary_employee is None:
        logger.info("Creating session-persistent employee...")
        session.primary_employee = _create_employee_via_ui(
            playwright, admin_credentials, QA_PRESET
        )

    yield session.primary_employee

    # Cleanup at end of session
    if session.primary_employee is not None:
        logger.info(f"Session cleanup: Deleting {session.primary_employee.full_name}...")
        _delete_employee_via_ui(
            playwright, admin_credentials, session.primary_employee
        )
        session.reset()


@pytest.fixture
def test_employee(playwright, admin_credentials):
    """
    Fresh employee for each test - directly usable!

    Created before the test, deleted after the test.
    """
    employee = _create_employee_via_ui(playwright, admin_credentials, QA_PRESET)

    yield employee

    # Teardown
    # TODO: Improve cleanup reliability (demo site may reset before deletion)
    logger.info(f"Cleanup: Deleting {employee.full_name}...")
    _delete_employee_via_ui(playwright, admin_credentials, employee)


# =============================================================================
# FACTORY FUNCTION for Employee Creation
# =============================================================================

def _create_employee_via_ui(
        playwright_instance,
        admin_creds: tuple,
        preset: EmployeePreset,
) -> Employee:
    """
    Creates an employee via the PIM UI in a temporary browser.

    Uses a separate browser instance to not interfere with test browser.

    Args:
        playwright_instance: Playwright session object.
        admin_creds: Tuple of (username, password) for admin login.
        preset: EmployeePreset with name configuration.

    Returns:
        Employee data object with all relevant fields.
    """
    from framework.pages.login_module.login_page import LoginPage
    from framework.system_config import BASE_URL

    unique_id = str(uuid.uuid4())[:8]
    first_name = f"{preset.name_prefix}_{unique_id}"
    last_name = preset.last_name_prefix

    username, password = admin_creds

    # Open a temporary headless browser for setup
    browser = playwright_instance.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)

    try:
        # Login as admin
        login_page = LoginPage(page)
        dashboard = login_page.login_with_credentials(username, password)

        # Navigate to PIM > Add Employee
        employee_list = dashboard.click_pim()
        add_page = employee_list.click_add_employee()

        # Fill form and save
        employee = add_page.create_employee(first_name, last_name)

        logger.info(f"Test employee created: {employee.full_name} (ID: {employee.employee_id})")
        return employee

    finally:
        browser.close()


def _delete_employee_via_ui(
        playwright_instance,
        admin_creds: tuple,
        employee: Employee,
) -> None:
    """
    Deletes an employee via the PIM UI in a temporary browser.

    Args:
        playwright_instance: Playwright session object.
        admin_creds: Tuple of (username, password) for admin login.
        employee: Employee to delete.
    """
    from framework.pages.login_module.login_page import LoginPage

    username, password = admin_creds

    browser = playwright_instance.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)

    try:
        login_page = LoginPage(page)
        dashboard = login_page.login_with_credentials(username, password)

        employee_list = dashboard.click_pim()
        employee_list.search_by_employee_name(employee.full_name)
        employee_list.delete_employee_by_name(
            employee.first_name, employee.last_name
        )
        logger.info(f"Test employee deleted: {employee.full_name}")

    except Exception as e:
        logger.warning(f"Employee deletion failed: {e}")
    finally:
        browser.close()
