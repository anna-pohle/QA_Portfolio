from __future__ import annotations
import logging

from playwright.sync_api import Page

from framework.pages.abstract_pages.base_page_w_sidebar import BasePageWithSidebar
from framework.pages.components.datepicker import DatepickerComponent
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class AssignLeavePage(BasePageWithSidebar):
    """
    Page Object for the Assign Leave form.

    Allows assigning leave to an employee with date range and leave type.
    """

    URL = f"{BASE_URL}/leave/assignLeave"

    def __init__(self, page: Page):
        """Initializes Assign Leave form locators.

        Args:
            page: Playwright Page object.
        """
        super().__init__(page)

        # Locators - Form Fields
        self.employee_name_input = self.page.get_by_placeholder("Type for hints...")
        self.leave_type_dropdown_icon = self.page.locator("form i").first
        self.from_date_input = self.page.locator(".oxd-date-input input").first
        self.to_date_input = self.page.locator(".oxd-date-input input").nth(1)
        self.comment_textarea = self.page.locator("textarea.oxd-textarea")

        # Locators - Actions
        self.assign_button = self.page.get_by_role("button", name="Assign")

        # Locators - Feedback
        self.success_toast = self.page.locator(".oxd-toast--success")
        self.confirm_dialog = self.page.locator(".oxd-dialog-sheet")
        self.confirm_ok_button = self.page.get_by_role("button", name="Ok")

        # Datepicker Components
        self._from_datepicker = DatepickerComponent(
            page, self.from_date_input
        )
        self._to_datepicker = DatepickerComponent(
            page, self.to_date_input
        )

        logger.info("Opened Assign Leave Page")

    # METHODS

    def select_employee(self, full_name: str) -> AssignLeavePage:
        """
        Selects an employee from the autocomplete field.

        Args:
            full_name: Full name of the employee.

        Returns:
            AssignLeavePage Page Object.
        """
        logger.info(f"Selecting employee: {full_name}")
        self.employee_name_input.click()
        self.employee_name_input.fill(full_name)

        # Wait for autocomplete and select first matching option
        option = self.page.get_by_role("option", name=full_name).first
        option.click(timeout=EXTENDED_TIMEOUT)

        return self

    def select_leave_type(self, leave_type: str) -> AssignLeavePage:
        """
        Selects a leave type from the dropdown.

        Args:
            leave_type: Leave type name (e.g. "CAN - Vacation").

        Returns:
            AssignLeavePage Page Object.
        """
        logger.info(f"Selecting leave type: {leave_type}")
        self.leave_type_dropdown_icon.click()
        self.page.get_by_role("option", name=leave_type).click()

        return self

    def set_date_range(self, from_date: str, to_date: str) -> AssignLeavePage:
        """
        Sets the leave date range.

        Args:
            from_date: Start date in format "YYYY-MM-DD".
            to_date: End date in format "YYYY-MM-DD".

        Returns:
            AssignLeavePage Page Object.
        """
        logger.info(f"Setting date range: {from_date} to {to_date}")
        self._from_datepicker.select_date(from_date)
        self._to_datepicker.select_date(to_date)

        return self

    def add_comment(self, comment: str) -> AssignLeavePage:
        """
        Adds a comment to the leave request.

        Args:
            comment: Comment text.

        Returns:
            AssignLeavePage Page Object.
        """
        logger.info("Adding comment to leave request")
        self.comment_textarea.fill(comment)
        return self

    def click_assign(self) -> AssignLeavePage:
        """Clicks the Assign button and handles confirmation dialog."""
        logger.info("Assigning leave...")
        self.assign_button.click()

        # OrangeHRM sometimes shows a confirmation dialog
        try:
            self.confirm_ok_button.click(timeout=EXTENDED_TIMEOUT)
            logger.info("Confirmed leave assignment dialog")
        except Exception:
            logger.debug("No confirmation dialog appeared")

        # Wait for success toast
        self.success_toast.wait_for(state="visible", timeout=EXTENDED_TIMEOUT)
        logger.info("Leave assigned successfully")

        return self

    def assign_leave(
            self,
            employee_name: str,
            leave_type: str,
            from_date: str,
            to_date: str,
            comment: str = ""
    ) -> AssignLeavePage:
        """
        Complete leave assignment flow.

        Args:
            employee_name: Full name of the employee.
            leave_type: Leave type name (e.g. "CAN - Vacation").
            from_date: Start date in format "YYYY-MM-DD".
            to_date: End date in format "YYYY-MM-DD".
            comment: Optional comment.

        Returns:
            AssignLeavePage Page Object.
        """
        (self
         .select_employee(employee_name)
         .select_leave_type(leave_type)
         .set_date_range(from_date, to_date))

        if comment:
            self.add_comment(comment)

        self.click_assign()

        return self
