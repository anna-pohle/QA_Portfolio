from __future__ import annotations
from typing import TYPE_CHECKING
from components.navbar import Navbar
from components.header import Header


if TYPE_CHECKING:
    from pages.base_page import BasePage
    from pages.checkout_page import CheckoutPage
    from pages.product_page import ProductPage


class StorePage(BasePage):
    URL = "https://grocerymate.masterschool.com/store"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)  # Header als Component
        self.navbar = Navbar(page)  # Navbar als Component


    # Methoden
    def go_to_storepage(self) -> StorePage:
        super().navigate(self.URL)  # Direkter Aufruf möglich
        return StorePage(self.page)

    def _get_product_card(self, product_name: str):
        """Hilfsfunktion: findet die Produktkarte anhand des Alt-Textes des Produktbildes
        Alle Buttons und Textfelder, die auf diese Funktion zugreifen, suchen nicht auf
        der gesamten Seite, sondern nur auf der Produktkarte.
        """
        product_card = self.page.locator(".card").filter(has=self.page.get_by_alt_text(product_name))
        return product_card

    def go_to_product_page(self, product_name: str) -> ProductPage:
        # Öffnet die Detailseite des gewünschten Produktes
        product_card = self._get_product_card(product_name)
        product_card.click()
        return ProductPage(self.page)

    def add_to_cart(self, product_name: str, quantity: int = 1) -> StorePage:
        # Fügt die gewünschte Menge (default =1) zum Warenkorb hinzu
        product_card = self._get_product_card(product_name)
        product_card.locator("input.quantity").fill(str(quantity))
        product_card.get_by_role("button", name="Add to Cart").click()
        return StorePage(self.page)

    def add_to_favorites(self, product_name: str) -> StorePage:
        product_card = self._get_product_card(product_name)
        product_card.get_by_role("button", name="❤").click()
        return StorePage(self.page)

    def go_to_cart(self) -> CheckoutPage:
        # Öffnet die Warenkorb-Ansicht
        self.header.click_cart()
        return CheckoutPage(self.page)

