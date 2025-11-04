from pages.base_page import BasePage
from pages.home_page import HomePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locator
        self.review_stars = page.locator(".interactive-rating .star")
        self.review_textarea = page.locator("textarea.new-review-form-control")
        self.send_button = page.get_by_role("button", name="Send")

    # Methoden
    def select_rating(self, stars: int) -> ProductPage:
        # Wählt eine Sternebewertung zwischen 1 und 5
        if not 1 <= stars <= 5:
            raise ValueError("Rating muss zwischen 1 und 5 sein")
        # Klicke auf den n-ten Stern (Index beginnt bei 0)
        self.review_stars.nth(stars - 1).click()
        return ProductPage(self.page)

    def write_review(self, text: str) -> ProductPage:
        # Füllt Review-Textfeld aus
        self.review_textarea.fill(text)
        return ProductPage(self.page)

    def rate_product(self, stars: int, text: str="") -> HomePage:
        self.select_rating(stars)
        self.write_review(text)
        self.send_button.click()
        return HomePage(self.page)
