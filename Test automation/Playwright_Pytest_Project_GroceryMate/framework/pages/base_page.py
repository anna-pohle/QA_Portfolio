from playwright.sync_api import Page
from framework.system_config import BASE_URL, BROWSER_CONFIG, EXTENDED_TIMEOUT


class BasePage:
    URL = None  # Muss von Subclass definiert werden

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

    def is_loaded(self) -> bool:
        # Prüft ob die Page geladen ist anhand ihrer URL, Subpages müssen URL-Attribut definieren
        if self.URL is None:
            raise NotImplementedError("Subclass muss URL definieren")

        try:
            # Prüfe URL
            self.page.wait_for_url(self.URL, timeout=EXTENDED_TIMEOUT)
            return True
        except TimeoutError:
            return False

    #HELPER-METHODE (privat!)
    def _extract_product_id_from_url(self) -> str:
        """
        Extrahiert product_id aus aktueller URL (wenn vorhanden)
        Funktioniert in jeder Page, sobald URL /product/{id} enthält
        """
        current_url = self.page.url
        if "/product/" not in current_url:
            raise ValueError(f"URL enthält kein Produktmuster: {current_url}")
        return current_url.split("/product/")[-1].split("?")[0]