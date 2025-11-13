from __future__ import annotations
from typing import TYPE_CHECKING
from framework.pages.base_page import BasePage
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT


if TYPE_CHECKING:
    from framework.pages.base_page import BasePage
    from framework.pages.home_page import HomePage


class ProductPage(BasePage):
    URL = f"{BASE_URL}/product"

    def __init__(self, page, product_id: str = None):
        super().__init__(page)
        self.product_id = product_id

        # Locator
        self.review_stars = page.locator(".interactive-rating .star")
        self.review_textarea = page.locator("textarea.new-review-form-control")
        self.send_button = page.get_by_role("button", name="Send")

    # Methoden
    def get_current_product_id(self) -> str:
        # extrahiert product_id aus aktueller URL unter Nutzung der Methode aus der BasePage
        return self._extract_product_id_from_url()

    def is_loaded(self, expected_product_id: str = None) -> bool:
        # Prüft, ob jeweilige product page geladen wurde
        # Optionales Argument: eine spezifische Produkt-ID
        # Nutzt self.product_id wenn kein Parameter übergeben
        check_id = expected_product_id or self.product_id

        try:
            if check_id:
                # Prüfe spezifische URL
                expected_url = f"{self.URL}/{check_id}"
                self.page.wait_for_url(expected_url, timeout=EXTENDED_TIMEOUT)
            else:
                # Prüfe Pattern (beliebige ID)
                self.page.wait_for_url(f"{self.URL}/*", timeout=EXTENDED_TIMEOUT)
            return True

        except TimeoutError:
            return False

    def select_rating(self, stars: int) -> "ProductPage":
        # Wählt eine Sternebewertung zwischen 1 und 5
        if not 1 <= stars <= 5:
            raise ValueError("Rating muss zwischen 1 und 5 sein")
        # Klicke auf den n-ten Stern (Index beginnt bei 0)
        self.review_stars.nth(stars - 1).click()
        return ProductPage(self.page)

    def write_review(self, text: str) -> "ProductPage":
        # Füllt Review-Textfeld aus
        self.review_textarea.fill(text)
        return ProductPage(self.page)

    def rate_product(self, stars: int, text: str = "") -> "HomePage":
        self.select_rating(stars)
        self.write_review(text)
        self.send_button.click()
        return HomePage(self.page)
