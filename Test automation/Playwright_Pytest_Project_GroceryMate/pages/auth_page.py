from __future__ import annotations
from typing import TYPE_CHECKING
from pages.base_page import BasePage
from pages.home_page import HomePage
if TYPE_CHECKING:
    from pages.home_page import HomePage



class AuthPage(BasePage):
    #Klassenattribut
    URL = "https://grocerymate.masterschool.com/auth"

    def __init__(self, page):
        super().__init__(page)

        #Locators
        self.email_input_field = self.page.locator("input[type='email']")
        self.password_input_field = self.page.locator("input[type='password']")
        self.name_input_field = self.page.get_by_placeholder("Full Name")

        self.sign_in_button = self.page.get_by_role("button", name="Sign In")
        self.sign_up_button = self.page.get_by_role("button", name="Sign Up")
        self.create_account_link = self.page.get_by_role("link", name="Create a new account")
        self.logout_button = self.page.get_by_role("button", name="Logout")

    #Methods
    def go_to_login(self) -> AuthPage:
        super().navigate(self.URL)
        return AuthPage(self.page)

    def login(self, email, password) -> HomePage:
        self.navigate(self.URL)
        self.email_input_field.fill(email)
        self.password_input_field.fill(password)
        self.sign_in_button.click()
        return HomePage(self.page)

    def create_account(self, email, password, name) -> AuthPage :
        self.navigate(self.URL)
        self.create_account_link.click()
        self.email_input_field.fill(email)
        self.password_input_field.fill(password)
        self.name_input_field.fill(name)
        self.sign_up_button.click()
        return self

    def logout(self, logout_button) -> AuthPage:
        self.navigate(self.URL)
        self.logout_button.click()
        return self

