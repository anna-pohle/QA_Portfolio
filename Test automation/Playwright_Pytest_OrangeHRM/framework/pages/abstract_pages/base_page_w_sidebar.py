from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from playwright.sync_api import Page, Locator, TimeoutError

from framework.pages.abstract_pages.base_page import BasePage
from framework.system_config import DEFAULT_TIMEOUT

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from framework.pages.pim_module.employee_list_page import EmployeeListPage
    from framework.pages.pim_module.add_employee_page import AddEmployeePage
    from framework.pages.leave_module.leave_list_page import LeaveListPage
    from framework.pages.leave_module.assign_leave_page import AssignLeavePage
    from framework.pages.dashboard_module.dashboard_page import DashboardPage


class BasePageWithSidebar(BasePage):
    """
    Base class for all pages with sidebar navigation.

    Extends BasePage with sidebar menu items and top bar elements
    (user dropdown, breadcrumb).
    """

    URL = None  # URL must be defined by subclass

    def __init__(self, page: Page):
        """Initializes sidebar and top bar locators.

        Args:
            page: Playwright Page object.
        """
        super().__init__(page)

        # Sidebar Locators
        self.sidebar = self.page.locator("aside.oxd-sidepanel")
        self.sidebar_search = self.sidebar.locator("input.oxd-input")

        # Top Bar Locators
        self.breadcrumb_title = self.page.locator(".oxd-topbar-header-title h6")
        self.user_dropdown_icon = self.page.get_by_role(
            "banner"
        ).get_by_role("img", name="profile picture")

    # SIDEBAR NAVIGATION

    def click_pim(self) -> EmployeeListPage:
        """Navigates to PIM (Employee List) via sidebar."""
        import framework.pages.pim_module.employee_list_page as pim_module

        logger.info("Navigating to: PIM")
        self.page.get_by_role("link", name="PIM").click()

        return pim_module.EmployeeListPage(self.page)

    def click_leave(self) -> LeaveListPage:
        """Navigates to Leave List via sidebar."""
        import framework.pages.leave_module.leave_list_page as leave_module

        logger.info("Navigating to: Leave")
        self.page.get_by_role("link", name="Leave", exact=True).click()

        return leave_module.LeaveListPage(self.page)

    def click_dashboard(self) -> DashboardPage:
        """Navigates to Dashboard via sidebar."""
        from framework.pages.dashboard_module.dashboard_page import DashboardPage

        logger.info("Navigating to: Dashboard")
        self.page.get_by_role("link", name="Dashboard").click()

        return DashboardPage(self.page)

    # TOP BAR METHODS

    def get_page_title(self) -> str:
        """Returns the current page title from the breadcrumb."""
        return self.breadcrumb_title.text_content().strip()

    def click_user_dropdown(self) -> BasePageWithSidebar:
        """Opens the user dropdown in the top bar."""
        self.user_dropdown_icon.click()
        return self

    def logout(self):
        """Logs out and returns to the Login page."""
        from framework.pages.login_module.login_page import LoginPage

        logger.info("Logging out...")
        self.click_user_dropdown()
        self.page.get_by_role("menuitem", name="Logout").click()

        return LoginPage(self.page)
