from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locator
        self.fav_button = self.page.

    # Methoden
    def rate_product(self, rating):
        self.page.get_by_placeholder("Your rating").fill(rating)
        self.page.get_by_text("Submit").click()
        return self
