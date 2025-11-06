from __future__ import annotations
from typing import TYPE_CHECKING
from components.navbar import Navbar
from components.header import Header
from pages.base_page import BasePage

if TYPE_CHECKING:
    from pages.store_page import StorePage
    from pages.auth_page import AuthPage

class HomePage(BasePage):
    URL = "https://grocerymate.masterschool.com"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)  # Header als Component
        self.navbar = Navbar(page) # Navbar als Component

    # Methoden
    def go_to_homepage(self) -> HomePage:
        self.navigate(self.URL)  # Direkter Aufruf der Homepage per URL
        return HomePage(self.page)

    # Methoden, die components nutzen
    def go_to_login(self) -> AuthPage:
        self.header.click_auth()  # Nutzt Header-Component
        return AuthPage(self.page)

    def go_to_store_page(self) -> StorePage:
        self.navbar.click_store()
        return StorePage(self.page)