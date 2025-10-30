# registration page elements & actions
from pages.base_page import BasePage, DEFAULT_TIMEOUT
from pages.store_page import StorePage

class AuthPage(BasePage):
    #Klassenattribut
    URL = "https://grocerymate.masterschool.com/auth"

    #Locators
    EMAIL_INPUT_FIELD = "input[type='email']"

    emailField: Locator = page.locator("input[type='email']")
    emailField.fill()


    PASSWORD_INPUT_FIELD = "input[type='password']"
    NAME_INPUT_FIELD = "input[placeholder='Full Name']"

    SIGN_IN_BUTTON = "button[type='submit']"
    CREATE_ACCOUNT_LINK = "role=link[name='Create a new account']"


    #Methods

    #extern
    def login(self, email, password) -> StorePage:
        self.navigate(self.URL)
        self.page.fill(self.EMAIL_INPUT_FIELD, email)
        self.page.fill(self.PASSWORD_INPUT_FIELD, password)
        self.page.click(self.SIGN_IN_BUTTON)
        return StorePage(self.page)


    def create_account(self, email, password, name) -> None:
        self.navigate(self.URL)
        self.page.click(self.CREATE_ACCOUNT_LINK)
        self.page.fill(self.EMAIL_INPUT_FIELD, email)
        self.page.fill(self.PASSWORD_INPUT_FIELD, password)
        self.page.fill(self.NAME_INPUT_FIELD, name)
        self.page.click(self.SIGN_IN_BUTTON)

