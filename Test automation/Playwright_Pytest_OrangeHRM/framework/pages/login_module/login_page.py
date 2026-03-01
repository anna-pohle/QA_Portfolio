from __future__ import annotations
import logging

from playwright.sync_api import Page

from framework.pages.abstract_pages.base_page import BasePage
from framework.pages.dashboard_module.dashboard_page import DashboardPage
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """
    Page Object for the Login page.

    Supports normal login and invalid login verification.
    """

    URL = f"{BASE_URL}/auth/login"

    def __init__(self, page: Page):
        super().__init__(page)

        # Locators - Login Form
        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")

        # Locators - Error Messages
        self.invalid_credentials_alert = self.page.locator("p.oxd-alert-content-text")
        self.required_field_error = self.page.locator("span.oxd-input-field-error-message")

        logger.info("Opened Login Page")

    # METHODS

    def go_to_login(self) -> LoginPage:
        """Navigates to the Login page."""
        super().navigate(self.URL)
        return LoginPage(self.page)

    def login_with_credentials(self, username: str, password: str) -> DashboardPage:
        """
        Login with username and password.

        Args:
            username: Login name.
            password: Password in plain text.

        Returns:
            DashboardPage Page Object.
        """
        logger.info(f"Started Login with User: {username}")
        self.navigate(self.URL)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        return DashboardPage(self.page)

    def login_with_invalid_credentials(self, username: str, password: str) -> LoginPage:
        """
        Attempts login with invalid credentials.

        Does NOT navigate away from the login page.

        Args:
            username: Invalid login name.
            password: Invalid password.

        Returns:
            LoginPage Page Object (stays on login page).
        """
        logger.info(f"Attempting invalid login with User: {username}")
        self.navigate(self.URL)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        return self

    def get_error_message(self) -> str:
        """Returns the error message text after failed login."""
        self.invalid_credentials_alert.wait_for(
            state="visible", timeout=EXTENDED_TIMEOUT
        )
        return self.invalid_credentials_alert.text_content().strip()

    def has_required_field_errors(self) -> bool:
        """Checks if 'Required' field validation errors are visible."""
        return self.required_field_error.first.is_visible()
