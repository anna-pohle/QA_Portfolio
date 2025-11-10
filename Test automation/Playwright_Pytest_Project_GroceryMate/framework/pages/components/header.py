from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.pages.checkout_page import CheckoutPage
    from framework.pages.auth_page import AuthPage
    from framework.pages.product_page import ProductPage


class Header:
    def __init__(self, page):
        self.page = page
        self.auth_button = page.locator('svg path[d*="M12 2a5"]').locator("..")
        self.cart_icon = page.locator('svg path[d*="M0 2.5A"]').locator("..")
        self.search_field = page.get_by_role("textbox", name="Search Products")
        self.suggestion_item = page.locator(".suggestion-item")

    def click_auth(self) -> AuthPage:
        self.auth_button.click()
        return AuthPage(self.page)

    def click_cart(self) -> CheckoutPage:
        self.cart_icon.click()
        return CheckoutPage(self.page)

    def search_item(self, item: str) -> ProductPage:
        self.search_field.fill(item)
        self.page.suggestion_item.filter(has_text=item).click()
        return ProductPage(self.page)