from __future__ import annotations
import logging

from playwright.sync_api import Page

from framework.pages.abstract_pages.base_page_w_sidebar import BasePageWithSidebar
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class DashboardPage(BasePageWithSidebar):
    """
    Page Object for the Dashboard.

    Shows the main overview after login.
    """

    URL = f"{BASE_URL}/dashboard/index"

    def __init__(self, page: Page):
        """Initializes Dashboard locators.

        Args:
            page: Playwright Page object.
        """
        super().__init__(page)

        # Wait for dashboard URL after login redirect
        self.page.wait_for_url(f"**{self.URL}**", timeout=EXTENDED_TIMEOUT)
        logger.info("Opened Dashboard")

        # Locators - Quick Launch Widgets
        self.quick_launch_section = self.page.locator(
            ".orangehrm-dashboard-grid"
        )

    # METHODS

    def get_dashboard_title(self) -> str:
        """Returns the Dashboard page title from the breadcrumb."""
        return self.get_page_title()
