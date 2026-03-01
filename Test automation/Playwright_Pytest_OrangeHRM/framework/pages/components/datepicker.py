import logging

from playwright.sync_api import Page, Locator

from framework.system_config import SHORT_TIMEOUT, EXTENDED_TIMEOUT

logger = logging.getLogger(__name__)


class DatepickerComponent:
    """
    Reusable datepicker component.

    Encapsulates navigation and selection in the OrangeHRM (oxd) datepicker.
    Can be used by different pages.
    """

    MONTH_NAMES = {
        "01": "January", "02": "February", "03": "March",
        "04": "April", "05": "May", "06": "June",
        "07": "July", "08": "August", "09": "September",
        "10": "October", "11": "November", "12": "December"
    }

    def __init__(self, page: Page, date_input: Locator):
        """
        Initializes the Datepicker component.

        Args:
            page: Playwright Page object.
            date_input: Locator for the date input field that opens the datepicker.
        """
        self.page = page
        self.date_input = date_input

        # Locators - Calendar Navigation
        self.calendar_popup = self.page.locator(".oxd-calendar-wrapper")
        self.month_selector = self.page.locator(".oxd-calendar-selector-month")
        self.year_selector = self.page.locator(".oxd-calendar-selector-year")
        self.prev_month_button = self.page.locator(
            ".oxd-calendar-header button:first-child"
        )
        self.next_month_button = self.page.locator(
            ".oxd-calendar-header button:last-child"
        )

    def select_date(self, date: str) -> None:
        """
        Selects a date in the datepicker.

        Args:
            date: Date in format "YYYY-MM-DD".
        """
        logger.info(f"Selecting date: {date}")

        year, month, day = date.split("-")
        target_month = self.MONTH_NAMES[month]
        target_year = year

        # Open datepicker by clicking the input
        self.date_input.click()
        self.calendar_popup.wait_for(state="visible", timeout=SHORT_TIMEOUT)

        # Reverse-mapping: "January" -> 1, etc.
        name_to_num = {v: int(k) for k, v in self.MONTH_NAMES.items()}

        # Navigate to the correct month/year (forward or backward)
        for attempt in range(24):
            current_month = self.month_selector.text_content().strip()
            current_year = self.year_selector.text_content().strip()

            logger.debug(
                f"Datepicker (attempt {attempt}): "
                f"'{current_month} {current_year}' (target: '{target_month} {target_year}')"
            )

            if current_month == target_month and current_year == target_year:
                break

            # Determine direction: compare current vs. target
            cur_y, cur_m = int(current_year), name_to_num.get(current_month, 0)
            tgt_y, tgt_m = int(target_year), int(month)

            if (cur_y, cur_m) < (tgt_y, tgt_m):
                self.next_month_button.click()
            else:
                self.prev_month_button.click()

        # Select the day
        day_button = self.page.locator(
            f".oxd-calendar-date:not(.--other-month)"
        ).get_by_text(str(int(day)), exact=True)
        day_button.click()

        # After selection the datepicker closes automatically.
        # Playwright's auto-wait ensures subsequent interactions
        # only start when the UI is ready.
        self.calendar_popup.wait_for(state="hidden", timeout=SHORT_TIMEOUT)
