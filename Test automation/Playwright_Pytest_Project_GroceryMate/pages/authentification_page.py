# registration page elements & actions
from base_page import BasePage


class AuthPage(BasePage):
    #Klassenattribut
    URL = "https://grocerymate.masterschool.com/auth"

    #Locators
    EMAIL_INPUT_FIELD = "input[type='email']"
    PASSWORD_INPUT_FIELD = "input[type='password']"
    NAME_INPUT_FIELD = "input[name='Full Name']"

    SIGN_IN_BUTTON = "button[type='submit']"
    CREATE_ACCOUNT_LINK = "role=link[name='Create a new account']"


    #Methods

    #intern
    def _enter_login_data(self, email, password, name=None):
        self.page.fill(self.EMAIL_INPUT_FIELD, email)
        self.page.fill(self.PASSWORD_INPUT_FIELD, password)
        if name and self.is_visible(self.NAME_INPUT_FIELD):
            self.page.fill(self.NAME_INPUT_FIELD, name)


    #extern
    def login(self, email, password):
        self.navigate(self.URL)
        self._enter_login_data(email, password)
        self.page.click(self.SIGN_IN_BUTTON)


    def create_account(self, email, password, name):
        self.navigate(self.URL)
        self.page.click(self.CREATE_ACCOUNT_LINK)
        self._enter_login_data(email, password, name)
        self.page.click(self.SIGN_IN_BUTTON)
