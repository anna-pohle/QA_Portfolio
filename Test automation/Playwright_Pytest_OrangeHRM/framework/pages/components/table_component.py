import logging

from playwright.sync_api import Page, Locator

from framework.system_config import EXTENDED_TIMEOUT, SHORT_TIMEOUT

logger = logging.getLogger(__name__)


class TableComponent:
    """
    Reusable component for OrangeHRM record tables.

    Encapsulates row access, counting, and wait logic for the
    oxd-table used across PIM, Leave, Admin, etc.
    """

    def __init__(self, page: Page):
        """
        Initializes the Table component.

        Args:
            page: Playwright Page object.
        """
        self.page = page

        # Locators
        self.table_container = self.page.locator("div.orangehrm-paper-container")
        self.table_body = self.page.locator(".oxd-table-body")
        self.table_rows = self.page.locator(
            ".oxd-table-body > .oxd-table-card"
        )
        self.records_count_label = self.page.locator(
            ".orangehrm-horizontal-padding span"
        )
        self.loading_spinner = self.page.locator(
            ".oxd-loading-spinner-container"
        )

    def get_row_count(self) -> int:
        """
        Returns the number of visible rows in the table.

        Returns 0 if the 'No Records Found' message is displayed.

        Returns:
            Number of table rows.
        """
        self.wait_for_loaded()

        # OrangeHRM hides the table body when no results are found
        if not self.table_body.is_visible():
            logger.debug("Table body hidden — no records found")
            return 0

        count = self.table_rows.count()
        logger.debug(f"Table row count: {count}")
        return count

    def get_all_rows(self) -> list[Locator]:
        """
        Returns all row Locators from the table.

        Returns:
            List of Locator objects for each table row.
        """
        self.wait_for_loaded()
        count = self.table_rows.count()
        return [self.table_rows.nth(i) for i in range(count)]

    def get_records_found_text(self) -> str:
        """
        Returns the 'Records Found' label text.

        Returns:
            Text like "(50) Records Found".
        """
        return self.records_count_label.text_content().strip()

    def wait_for_loaded(self) -> None:
        """Waits until the table has finished loading (spinner gone).

        Handles both cases: table with rows, and 'No Records Found'.
        """
        try:
            self.loading_spinner.wait_for(state="hidden", timeout=SHORT_TIMEOUT)
        except Exception:
            # Spinner may never appear if data loads quickly
            pass

        # Wait for either the table body OR the 'No Records Found' span
        self.page.locator(
            ".oxd-table-body, span.oxd-text:has-text('No Records Found')"
        ).first.wait_for(state="visible", timeout=EXTENDED_TIMEOUT)
