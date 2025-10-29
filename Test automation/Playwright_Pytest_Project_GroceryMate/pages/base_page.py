from playwright.sync_api import sync_playwright, Page, expect

URL = "https://grocerymate.masterschool.com/"
DEFAULT_TIMEOUT = 5000  # 5 Sekunden in Millisekunden

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = DEFAULT_TIMEOUT

    def navigate(self, URL: str):
        # Navigation zur URL
        self.page.goto(URL, timeout=self.timeout)
        self.page.wait_for_load_state("networkidle")

    def click(self, locator: str):
        # Element anklicken
        self.page.locator(locator).click(timeout=self.timeout)

    def fill(self, locator: str, text: str):
        # Text eingeben
        element = self.page.locator(locator)
        element.fill(text, timeout=self.timeout)

    def is_visible(self, locator: str) -> bool:
        # Sichtbarkeits-Check
        return self.page.locator(locator).is_visible(timeout=self.timeout)