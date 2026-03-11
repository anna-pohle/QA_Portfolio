import pytest
from framework.pages.login_module.login_page import LoginPage
from framework.system_config import BASE_URL


@pytest.mark.smoke
@pytest.mark.feature_login
def test_login(browser_page, admin_credentials):
    """
    Tests successful login with admin credentials.

    Verifies that the Dashboard loads after login.
    """
    username, password = admin_credentials

    # Act
    dashboard = (LoginPage(browser_page)
        .login_with_credentials(
            username=username,
            password=password
        ))

    # Assert: check if Dashboard loaded
    assert dashboard.is_loaded(), (
        f"Expected URL containing: '/dashboard/index', "
        f"actual URL: {browser_page.url}"
    )


@pytest.mark.smoke
@pytest.mark.feature_login
def test_login_invalid_credentials(browser_page):
    """
    Tests login with invalid credentials.

    Verifies that an error message is shown and user stays on login page.
    """
    # Act
    login_page = (LoginPage(browser_page)
        .login_with_invalid_credentials(
            username="InvalidUser",
            password="wrongpassword"
        ))

    # Assert: error message should be visible
    error_message = login_page.get_error_message()
    assert "Invalid credentials" in error_message, (
        f"Expected 'Invalid credentials' error, got: '{error_message}'"
    )


@pytest.mark.feature_login
def test_login_empty_fields(browser_page):
    """
    Tests login with empty fields.

    Verifies that 'Required' validation errors appear.
    """
    # Act - click login without filling fields
    login_page = LoginPage(browser_page)
    login_page.navigate(login_page.URL)
    login_page.login_button.click()

    # Assert: required field errors should be visible
    assert login_page.has_required_field_errors(), (
        "Expected 'Required' validation errors for empty fields"
    )
