import pytest
from framework.pages.login_module.login_page import LoginPage
from framework.dataclasses.leave_types import LeaveType
from framework.utils.date_utils import DateUtils
from tests.testdata.singleton import EmployeeSession


@pytest.mark.smoke
@pytest.mark.feature_leave
def test_assign_leave(browser_page, admin_credentials, session_employee):
    """
    TC-4.1: Assign leave to an employee.

    Uses session-persistent employee to assign vacation leave.
    Verifies that the assignment completes successfully (success toast).
    """
    username, password = admin_credentials

    # Get a unique future date (each test uses a different day)
    session = EmployeeSession()
    days_ahead = session.get_next_future_day()
    leave_date = DateUtils.get_date_x_days_from_now(days_ahead)

    # Act: Login > Leave > Assign Leave
    assign_leave_page = (
        LoginPage(browser_page)
        .login_with_credentials(username, password)
        .click_leave()
        .click_assign_leave()
        .assign_leave(
            employee_name=session_employee.full_name,
            leave_type=LeaveType.CAN_VACATION.value,
            from_date=leave_date,
            to_date=leave_date,
            comment="Automated test - single day vacation",
        )
    )

    # Assert: success toast was shown (verified inside assign_leave method)
    # If we get here without exception, the assignment was successful
    assert assign_leave_page.success_toast.is_visible(), (
        "Leave assignment did not show success confirmation"
    )


@pytest.mark.feature_leave
def test_assign_multi_day_leave(browser_page, admin_credentials, session_employee):
    """
    TC-4.2: Assign multi-day leave to an employee.

    Assigns personal leave spanning multiple days and verifies success.
    """
    username, password = admin_credentials

    session = EmployeeSession()
    start_day = session.get_next_future_day()
    from_date = DateUtils.get_date_x_days_from_now(start_day)
    to_date = DateUtils.get_date_x_days_from_now(start_day + 2)

    # Act: Login > Leave > Assign Leave (multi-day)
    assign_leave_page = (
        LoginPage(browser_page)
        .login_with_credentials(username, password)
        .click_leave()
        .click_assign_leave()
        .assign_leave(
            employee_name=session_employee.full_name,
            leave_type=LeaveType.CAN_PERSONAL.value,
            from_date=from_date,
            to_date=to_date,
            comment="Automated test - multi day personal leave",
        )
    )

    # Assert: success toast was shown
    assert assign_leave_page.success_toast.is_visible(), (
        "Multi-day leave assignment did not show success confirmation"
    )
