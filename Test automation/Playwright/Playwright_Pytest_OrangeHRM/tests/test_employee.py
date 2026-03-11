import pytest
from framework.pages.login_module.login_page import LoginPage
from framework.utils.string_utils import StringUtils


@pytest.mark.smoke
@pytest.mark.feature_pim
def test_add_employee(browser_page, admin_credentials):
    """
    TC-3.1: Add a new employee via PIM module.

    Creates a new employee and verifies it appears in the employee list.
    Cleans up the created employee after the test.
    """
    username, password = admin_credentials

    # Unique name to avoid conflicts (demo resets periodically)
    unique_suffix = StringUtils.generate_random_string(6)
    first_name = f"TestQA_{unique_suffix}"
    last_name = "AutoTest"

    # Act: Login > PIM > Add Employee
    add_employee_page = (
        LoginPage(browser_page)
        .login_with_credentials(username, password)
        .click_pim()
        .click_add_employee()
    )

    employee = add_employee_page.create_employee(first_name, last_name)

    # Navigate back to Employee List and search for created employee
    employee_list = (
        add_employee_page
        .click_pim()
        .search_by_employee_name(f"{first_name} {last_name}")
    )

    # Assert: employee should exist in the filtered results
    assert employee_list.has_employee_in_list(
        first_name=first_name,
        last_name=last_name
    ), f"Employee '{first_name} {last_name}' not found in employee list"

    # Cleanup: delete the created employee
    employee_list.delete_employee_by_name(first_name, last_name)


@pytest.mark.smoke
@pytest.mark.feature_pim
def test_search_employee_by_name(browser_page, admin_credentials, test_employee):
    """
    TC-3.2: Search for an employee by name.

    Uses a dynamically created test employee (from fixture).
    Verifies the search filter returns matching results.
    """
    username, password = admin_credentials

    # Act: Login > PIM > Search
    employee_list = (
        LoginPage(browser_page)
        .login_with_credentials(username, password)
        .click_pim()
        .search_by_employee_name(test_employee.full_name)
    )

    # Assert: employee should be in the filtered results
    assert employee_list.has_employee_in_list(
        first_name=test_employee.first_name,
        last_name=test_employee.last_name
    ), f"Employee '{test_employee.full_name}' not found after search"


@pytest.mark.feature_pim
def test_search_returns_no_results(browser_page, admin_credentials):
    """
    TC-3.3: Search for a non-existent employee.

    Verifies the search filter shows 'No Records Found' or empty table.
    """
    username, password = admin_credentials

    # Act: Login > PIM > Search by ID (non-existent)
    employee_list = (
        LoginPage(browser_page)
        .login_with_credentials(username, password)
        .click_pim()
        .search_by_employee_id("99999999")
    )

    # Assert: no results
    record_count = employee_list.get_record_count()
    assert record_count == 0, (
        f"Expected 0 records for non-existent ID, got {record_count}"
    )
