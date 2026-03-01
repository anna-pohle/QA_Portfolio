from __future__ import annotations
import logging

from playwright.sync_api import Page

from framework.dataclasses.leave_types import LeaveStatus
from framework.pages.abstract_pages.base_page_w_sidebar import BasePageWithSidebar
from framework.pages.components.table_component import TableComponent
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class LeaveListPage(BasePageWithSidebar):
    """
    Page Object for the Leave List page.

    Provides access to leave records and navigation to sub-pages
    (Assign Leave, Apply Leave, Entitlements).
    """

    URL = f"{BASE_URL}/leave/viewLeaveList"

    def __init__(self, page: Page):
        """Initializes Leave List locators and table component.

        Args:
            page: Playwright Page object.
        """
        super().__init__(page)

        # Table component for leave records
        self._table = TableComponent(page)

        # Locators - Sub-Navigation
        self.assign_leave_link = self.page.get_by_role("link", name="Assign Leave")
        self.my_leave_link = self.page.get_by_role("link", name="My Leave")
        self.apply_link = self.page.get_by_role("link", name="Apply")

        # Locators - Filter
        self.search_button = self.page.get_by_role("button", name="Search")
        self.reset_button = self.page.get_by_role("button", name="Reset")

        logger.info("Opened Leave List Page")

    # NAVIGATION

    def click_assign_leave(self):
        """Navigates to the Assign Leave form."""
        from framework.pages.leave_module.assign_leave_page import AssignLeavePage

        logger.info("Navigating to: Assign Leave")
        self.assign_leave_link.click()

        return AssignLeavePage(self.page)

    # TABLE METHODS

    def get_record_count(self) -> int:
        """Returns the number of leave records found."""
        return self._table.get_row_count()

    def has_leave_entry(
            self,
            employee_name: str,
            leave_type: str,
            status: LeaveStatus
    ) -> bool:
        """
        Checks if a leave entry exists in the table.

        Args:
            employee_name: Full name of the employee.
            leave_type: Leave type string (e.g. "CAN - Vacation").
            status: Expected leave status.

        Returns:
            True if matching entry found, otherwise False.
        """
        logger.info(
            f"Checking for leave entry: {employee_name}, "
            f"{leave_type}, {status.value}"
        )

        rows = self._table.get_all_rows()
        for row in rows:
            cells = row.locator(".oxd-table-cell")

            # Column layout: Date | Employee Name | Leave Type | Leave Balance | Days | Status | Actions
            row_employee = cells.nth(1).text_content().strip()
            row_leave_type = cells.nth(2).text_content().strip()
            row_status = cells.nth(5).text_content().strip()

            if (employee_name in row_employee
                    and leave_type in row_leave_type
                    and status.value in row_status):
                logger.info(f"Found matching leave entry for {employee_name}")
                return True

        logger.info(f"Leave entry NOT found for {employee_name}")
        return False
