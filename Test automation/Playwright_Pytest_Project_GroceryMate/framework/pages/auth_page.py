from __future__ import annotations
from typing import TYPE_CHECKING
from framework.pages.base_page import BasePage
from framework.pages.home_page import HomePage
from framework.dataclasses.data_object_user import User
from framework.system_config import BASE_URL

if TYPE_CHECKING:
    from framework.pages.home_page import HomePage



class AuthPage(BasePage):
    # Klassenattribut
    URL = f"{BASE_URL}/auth"

    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.email_input_field = self.page.locator("input[type='email']")
        self.password_input_field = self.page.locator("input[type='password']")
        self.name_input_field = self.page.get_by_placeholder("Full Name")

        self.sign_in_button = self.page.get_by_role("button", name="Sign In")
        self.sign_up_button = self.page.get_by_role("button", name="Sign Up")
        self.create_account_link = self.page.get_by_role(
            "link", name="Create a new account"
        )
        self.logout_button = self.page.get_by_role("button", name="Logout")

    # Methods
    def go_to_login(self) -> AuthPage:
        super().navigate(self.URL)
        return AuthPage(self.page)

    def login(self, user: User) -> HomePage:
        self.navigate(self.URL)
        self.email_input_field.fill(user.email)
        self.password_input_field.fill(user.password)
        self.sign_in_button.click()
        return HomePage(self.page)

    def create_account(self, user: User) -> AuthPage:
        self.navigate(self.URL)
        self.create_account_link.click()
        self.name_input_field.fill(user.name)
        self.email_input_field.fill(user.email)
        self.password_input_field.fill(user.password)
        self.sign_up_button.click()
        success_toast = self.page.locator("text=Registration successful")
        success_toast.wait_for(state="visible")
        return self

    def logout(self) -> AuthPage:
        self.navigate(self.URL)
        self.logout_button.click()
        return self

