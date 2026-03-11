import logging

from playwright.sync_api import Page, expect
from framework.system_config import BASE_URL, BROWSER_CONFIG, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class BasePage:
    """
    Base class for all Page Objects.

    Provides basic methods for navigation and element interaction.
    All concrete page classes inherit from this class.

    Each Page Object has access to:
    - self.page: Playwright Page object
    - self.timeout: Default timeout from BROWSER_CONFIG
    - self.base_url: Base URL of the application
    """

    URL = None  # Must be defined by subclass

    def __init__(self, page: Page):
        """Initializes the base page with Playwright Page object.

        Args:
            page: Playwright Page object for browser interactions.
        """
        self.page = page
        self.timeout = BROWSER_CONFIG.get("timeout")
        self.base_url = BASE_URL

    # NAVIGATION

    def navigate(self, url: str):
        """Navigates to the given URL and waits for DOM readiness.

        Args:
            url: Target URL for navigation.
        """
        logger.debug(f"Navigating to: {url}")
        self.page.goto(url, timeout=EXTENDED_TIMEOUT)
        # domcontentloaded instead of networkidle: In an SPA, networkidle
        # often blocks due to WebSockets/Polling. Playwright's auto-wait
        # ensures that subsequent interactions only start when elements are ready.
        self.page.wait_for_load_state("domcontentloaded")
        return self

    def is_loaded(self) -> bool:
        """
        Checks if the page is loaded based on its URL.

        Subpages must define the URL attribute.

        Returns:
            True if the URL matches, otherwise False.
        """
        if self.URL is None:
            raise NotImplementedError("Subclass must define URL")

        try:
            self.page.wait_for_url(f"**{self.URL}**", timeout=EXTENDED_TIMEOUT)
            logger.debug(f"Page loaded: {self.URL}")
            return True
        except TimeoutError:
            logger.warning(
                f"Page load timeout - expected: {self.URL}, "
                f"actual: {self.page.url}"
            )
            return False

    # ELEMENT INTERACTION

    def click(self, locator: str):
        """Clicks on an element by locator."""
        logger.debug(f"Clicking element: {locator}")
        self.page.locator(locator).click(timeout=self.timeout)

    def fill(self, locator: str, text: str) -> None:
        """Fills an input field with the given text."""
        logger.debug(f"Filling element {locator} with text")
        element = self.page.locator(locator)
        element.fill(text, timeout=self.timeout)

    def is_visible(self, locator: str) -> bool:
        """Checks if an element is visible."""
        return self.page.locator(locator).is_visible(timeout=self.timeout)

    def wait_for_element(self, locator: str, state: str = "visible") -> None:
        """
        Waits until an element reaches the desired state.

        Args:
            locator: CSS selector or Playwright locator string.
            state: Expected state ("visible", "hidden", "attached", "detached").
        """
        self.page.locator(locator).wait_for(state=state, timeout=self.timeout)
