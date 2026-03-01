from __future__ import annotations
import logging

from playwright.sync_api import Page

from framework.pages.abstract_pages.base_page_w_sidebar import BasePageWithSidebar
from framework.pages.components.table_component import TableComponent
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class EmployeeListPage(BasePageWithSidebar):
    """
    Page Object for the PIM Employee List page.

    Provides search, filter, and navigation to Add Employee.
    """

    URL = f"{BASE_URL}/pim/viewEmployeeList"

    def __init__(self, page: Page):
        """Initializes Employee List locators and table component.

        Args:
            page: Playwright Page object.
        """
        super().__init__(page)

        # Table component for employee records
        self._table = TableComponent(page)

        # Locators - Search Filter
        self.employee_name_filter = self.page.locator(
            "div.oxd-table-filter .oxd-input-group"
        ).filter(has_text="Employee Name").get_by_placeholder("Type for hints...")
        self.employee_id_filter = self.page.locator(
            "div.oxd-table-filter .oxd-input-group"
        ).filter(has_text="Employee Id").locator("input")
        self.search_button = self.page.get_by_role("button", name="Search")
        self.reset_button = self.page.get_by_role("button", name="Reset")

        # Locators - Actions
        self.add_employee_button = self.page.locator(
            "div.orangehrm-header-container button"
        )

        logger.info("Opened Employee List Page")

    # NAVIGATION

    def click_add_employee(self):
        """Navigates to the Add Employee form."""
        from framework.pages.pim_module.add_employee_page import AddEmployeePage

        logger.info("Clicking Add Employee button")
        self.add_employee_button.click()

        return AddEmployeePage(self.page)

    # SEARCH METHODS

    def search_by_employee_name(self, name: str) -> EmployeeListPage:
        """
        Searches for an employee by name using the filter.

        Args:
            name: Employee name to search for.

        Returns:
            EmployeeListPage Page Object.
        """
        logger.info(f"Searching for employee: {name}")
        self.employee_name_filter.click()
        self.employee_name_filter.fill(name)

        # Wait for autocomplete suggestions and select first match
        autocomplete_option = self.page.get_by_role("option").first
        autocomplete_option.click(timeout=EXTENDED_TIMEOUT)

        self.search_button.click()

        # Wait for table to refresh (loading spinner disappears)
        self._wait_for_table_loaded()

        return self

    def search_by_employee_id(self, employee_id: str) -> EmployeeListPage:
        """
        Searches for an employee by ID.

        Args:
            employee_id: Employee ID to search for.

        Returns:
            EmployeeListPage Page Object.
        """
        logger.info(f"Searching for employee ID: {employee_id}")
        self.employee_id_filter.fill(employee_id)
        self.search_button.click()

        self._wait_for_table_loaded()

        return self

    def reset_search(self) -> EmployeeListPage:
        """Resets the search filter."""
        logger.info("Resetting search filter")
        self.reset_button.click()
        self._wait_for_table_loaded()
        return self

    # TABLE METHODS

    def get_record_count(self) -> int:
        """Returns the number of records found."""
        return self._table.get_row_count()

    def has_employee_in_list(self, first_name: str, last_name: str) -> bool:
        """
        Checks if an employee with the given name exists in the table.

        Args:
            first_name: First name of the employee.
            last_name: Last name of the employee.

        Returns:
            True if employee is found, otherwise False.
        """
        logger.info(f"Checking if employee exists: {first_name} {last_name}")

        rows = self._table.get_all_rows()
        for row in rows:
            cells = row.locator(".oxd-table-cell")
            # Column 3 = First (+ Middle) Name, Column 4 = Last Name
            row_first = cells.nth(2).text_content().strip()
            row_last = cells.nth(3).text_content().strip()

            if first_name in row_first and last_name == row_last:
                logger.info(f"Found employee: {first_name} {last_name}")
                return True

        logger.info(f"Employee NOT found: {first_name} {last_name}")
        return False

    def delete_employee_by_name(self, first_name: str, last_name: str) -> EmployeeListPage:
        """
        Deletes an employee from the list by name.

        Args:
            first_name: First name of the employee.
            last_name: Last name of the employee.

        Returns:
            EmployeeListPage Page Object.
        """
        logger.info(f"Deleting employee: {first_name} {last_name}")

        rows = self._table.get_all_rows()
        for row in rows:
            cells = row.locator(".oxd-table-cell")
            row_first = cells.nth(2).text_content().strip()
            row_last = cells.nth(3).text_content().strip()

            if first_name in row_first and last_name == row_last:
                # Click the trash icon button in the last cell
                row.locator("button i.bi-trash").click()

                # Confirm deletion in the dialog
                self.page.get_by_role("button", name="Yes, Delete").click(
                    timeout=EXTENDED_TIMEOUT
                )
                logger.info(f"Deleted employee: {first_name} {last_name}")
                break

        self._wait_for_table_loaded()
        return self

    # INTERNAL METHODS

    def _wait_for_table_loaded(self) -> None:
        """Waits until the table has finished loading."""
        self._table.wait_for_loaded()
