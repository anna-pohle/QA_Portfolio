from playwright.sync_api import Page
from system_config import BASE_URL, BROWSER_CONFIG

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = BROWSER_CONFIG.get("timeout")
        self.base_url = BASE_URL  # Speichere BASE_URL als Attribut

    def navigate(self, url: str):
        # Navigation zur URL
        self.page.goto(url, timeout=self.timeout)
        self.page.wait_for_load_state("networkidle")

    def click(self, locator: str) -> Page:
        # Element anklicken
        self.page.locator(locator).click(timeout=self.timeout)

    def fill(self, locator: str, text: str) -> None:
        # Text in Input-Feld eingeben
        element = self.page.locator(locator)
        element.fill(text, timeout=self.timeout)

    def is_visible(self, locator: str) -> bool:
        # Sichtbarkeits-Check
        return self.page.locator(locator).is_visible(timeout=self.timeout)

