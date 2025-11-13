from __future__ import annotations
from typing import TYPE_CHECKING
from framework.pages.base_page import BasePage
from framework.pages.components.navbar import Navbar
from framework.pages.components.header import Header
from framework.pages.product_page import ProductPage
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT

if TYPE_CHECKING:
    from framework.pages.checkout_page import CheckoutPage
    from framework.pages.product_page import ProductPage


class StorePage(BasePage):
    URL = f"{BASE_URL}/store"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)  # Header als Component
        self.navbar = Navbar(page)  # Navbar als Component
        self.product_cards = page.locator(".product-card")

    # HELPER-METHODEN (privat!)
    def _get_product_card(self, product_name: str):
        """Hilfsfunktion: findet eine spezifische Produktkarte anhand des Alt-Textes des Produktbildes
        Alle Buttons und Textfelder, die auf diese Funktion zugreifen, suchen nicht auf
        der gesamten Seite, sondern nur auf der Produktkarte mit dem angegebenen Produktnamen.
        """
        product_card = self.page.locator(".card").filter(
            has=self.page.get_by_alt_text(product_name)
        )
        return product_card

    def _click_product_image_and_get_page(self, product_card_locator) -> ProductPage:
        """
        Klickt auf Produktbild und erstellt ProductPage, aus der gleichzeitig die ID extrahiert wird
        (unter Nutzung der Methode aus der BasePage)

        Args:
            product_card_locator: Locator für die Produktkarte oder das Bild

        Returns:
            ProductPage mit gesetzter product_id
        """
        # Findet das Bild INNERHALB der übergebenen Karte
        product_image = product_card_locator.locator("img.card-img-top")
        product_image.click()

        # Wartet bis URL sich ändert
        self.page.wait_for_url("**/product/*", timeout=EXTENDED_TIMEOUT)

        # Extrahiert ID aus der NEUEN URL (mittels Methode aus BasePage)
        product_id = self._extract_product_id_from_url()

        # Erstelle ProductPage mit ID
        product_page = ProductPage(self.page, product_id=product_id)
        product_page.is_loaded(expected_product_id=product_id)

        return product_page

    # NAVIGATIONS-METHODEN
    def go_to_storepage(self) -> "StorePage":
        super().navigate(self.URL)  # Direkter Aufruf möglich
        return self

    def go_to_product_page(self, product_name: str) -> ProductPage:
        # Öffnet die Detailseite des gewünschten Produktes
        product_card = self._get_product_card(product_name)
        product_card.click()
        return ProductPage(self.page)

    def go_to_cart(self) -> "CheckoutPage":
        # Öffnet die Warenkorb-Ansicht
        self.header.click_cart()
        return CheckoutPage(self.page)

    # INTERAKTIONS-METHODEN
    def add_to_cart(self, product_name: str, quantity: int = 1) -> "StorePage":
        # Fügt die gewünschte Menge (default =1) zum Warenkorb hinzu
        product_card = self._get_product_card(product_name)
        product_card.locator("input.quantity").fill(str(quantity))
        product_card.get_by_role("button", name="Add to Cart").click()
        return StorePage(self.page)

    def add_to_favorites(self, product_name: str) -> "StorePage":
        product_card = self._get_product_card(product_name)
        product_card.get_by_role("button", name="❤").click()
        return StorePage(self.page)



