from __future__ import annotations
import logging

from playwright.sync_api import Page

from framework.dataclasses.data_object_employee import Employee
from framework.pages.abstract_pages.base_page_w_sidebar import BasePageWithSidebar
from framework.system_config import BASE_URL, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class AddEmployeePage(BasePageWithSidebar):
    """
    Page Object for the Add Employee form.

    Allows creating new employees via the PIM module.
    """

    URL = f"{BASE_URL}/pim/addEmployee"

    def __init__(self, page: Page):
        """Initializes Add Employee form locators.

        Args:
            page: Playwright Page object.
        """
        super().__init__(page)

        # Locators - Employee Form
        self.first_name_input = self.page.get_by_placeholder("First Name")
        self.middle_name_input = self.page.get_by_placeholder("Middle Name")
        self.last_name_input = self.page.get_by_placeholder("Last Name")
        self.employee_id_input = self.page.locator(
            ".oxd-input-group"
        ).filter(has_text="Employee Id").locator("input")

        # Locators - Actions
        self.save_button = self.page.get_by_role("button", name="Save")
        self.cancel_button = self.page.get_by_role("button", name="Cancel")

        # Locators - Login Details Toggle
        self.create_login_toggle = self.page.locator(".oxd-switch-input")

        # Locators - Success Toast
        self.success_toast = self.page.locator(".oxd-toast--success")

        logger.info("Opened Add Employee Page")

    # METHODS

    def fill_employee_form(
            self,
            first_name: str,
            last_name: str,
            middle_name: str = "",
            employee_id: str = ""
    ) -> AddEmployeePage:
        """
        Fills the employee creation form.

        Args:
            first_name: First name of the employee.
            last_name: Last name of the employee.
            middle_name: Middle name (optional).
            employee_id: Custom employee ID (optional, auto-generated if empty).

        Returns:
            AddEmployeePage Page Object.
        """
        logger.info(f"Filling employee form: {first_name} {last_name}")

        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)

        if middle_name:
            self.middle_name_input.fill(middle_name)

        if employee_id:
            self.employee_id_input.clear()
            self.employee_id_input.fill(employee_id)

        return self

    def get_employee_id(self) -> str:
        """Returns the (auto-generated) Employee ID from the form."""
        return self.employee_id_input.input_value()

    def click_save(self) -> AddEmployeePage:
        """Clicks the Save button and waits for success toast."""
        logger.info("Saving new employee...")
        self.save_button.click()

        # Wait for success toast OR page navigation
        self.success_toast.wait_for(state="visible", timeout=EXTENDED_TIMEOUT)
        logger.info("Employee saved successfully")

        return self

    def create_employee(self, first_name: str, last_name: str) -> Employee:
        """
        Creates a new employee and returns the Employee data object.

        Complete flow: fill form, grab employee ID, save.

        Args:
            first_name: First name of the employee.
            last_name: Last name of the employee.

        Returns:
            Employee data object with all relevant fields.
        """
        self.fill_employee_form(first_name, last_name)
        employee_id = self.get_employee_id()
        self.click_save()

        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            employee_id=employee_id,
            full_name=f"{first_name} {last_name}",
        )

        logger.info(f"Created employee: {employee.full_name} (ID: {employee.employee_id})")
        return employee
