from pages.base_page import BasePage
from pages.store_page import StorePage
from pages.auth_page import AuthPage
from components.header import Header
from components.navbar import Navbar

class HomePage(BasePage):
    URL = "https://grocerymate.masterschool.com"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)  # Header als Component
        self.navbar = Navbar(page) # Navbar als Component

    # Methoden
    def go_to_homepage(self):
        super().navigate(self.URL)  # Direkter Aufruf der Homepage per URL
        return self

    # Methoden, die components nutzen
    def go_to_login(self) -> AuthPage:
        return self.header.click_auth()  # Nutzt Header-Component

    def go_to_store_page(self) -> StorePage:
        return self.navbar.click_store()
