# registration page elements & actions
from base_page import BasePage


URL = "https://grocerymate.masterschool.com/auth"

class AuthPage(BasePage):
    #Locators
    EMAIL_INPUT_FIELD = "input[type='email']"
    PASSWORD_INPUT_FIELD = "input[type='password']"

    SIGN_IN_BUTTON = "button[type='submit']"
    CREATE_ACCOUNT_LINK = "role=link[name='Create a new account']"


    #Methods

    #intern
    def _enter_login_data(self, email, password):
        self.page.fill(self.EMAIL_INPUT_FIELD, email)
        self.page.fill(self.PASSWORD_INPUT_FIELD, password)

    #extern
    def login(self, email, password):
        self.navigate(URL)
        self._enter_login_data
        self.page.click(self.SIGN_IN_BUTTON)

    def create_account(self, email, password):
        self.navigate(URL)
        self._enter_login_data
        self.page.click(self.CREATE_ACCOUNT_LINK)