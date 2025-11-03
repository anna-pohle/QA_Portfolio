from pages.checkout_page import CheckoutPage
from pages.auth_page import AuthPage


class Header:
    def __init__(self, page):
        self.page = page
        self.auth_button = page.locator("")
        self.cart_icon = page.locator("")
        self.search_field = page.get_by_role("textbox", name="Search Products")

    def click_auth(self) -> AuthPage:
        self.auth_button.click()
        return AuthPage(self.page)

    def click_cart(self) -> CheckoutPage:
        self.cart_icon.click()
        return CheckoutPage(self.page)

    def search_item(self, item: str):
        self.search_field.fill(item)
        self.page.keyboard.press("Enter")