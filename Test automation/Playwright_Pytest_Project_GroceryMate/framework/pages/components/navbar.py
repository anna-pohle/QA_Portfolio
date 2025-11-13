from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.pages.store_page import StorePage
    from framework.pages.home_page import HomePage

class Navbar:
    def __init__(self, page):
        self.page = page
        self.store_button = self.page.get_by_role("link", name="Shop")
        self.home_button = self.page.get_by_role("link", name="Home")


    def click_store(self):
        self.store_button.click()
        return StorePage(self.page)

    def click_home(self):
        self.home_button.click()
        return HomePage(self.page)