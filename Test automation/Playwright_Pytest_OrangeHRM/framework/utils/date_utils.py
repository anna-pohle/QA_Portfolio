from datetime import datetime, timedelta


class DateUtils:
    """
    Utilities for date operations.

    Provides static methods for common date calculations.
    """

    @staticmethod
    def get_date_x_days_ago(days: int) -> str:
        """
        Returns the date X days in the past.

        Args:
            days: Number of days in the past (0 = today).

        Returns:
            Date in format "YYYY-MM-DD".
        """
        date = datetime.now() - timedelta(days)
        return date.strftime("%Y-%m-%d")

    @staticmethod
    def get_date_x_days_from_now(days: int) -> str:
        """
        Returns the date X days in the future.

        Args:
            days: Number of days in the future (1 = tomorrow).

        Returns:
            Date in format "YYYY-MM-DD".
        """
        date = datetime.now() + timedelta(days)
        return date.strftime("%Y-%m-%d")

    @staticmethod
    def get_last_weeks_monday() -> str:
        """
        Returns the Monday of last week.

        Returns:
            Date in format "YYYY-MM-DD".
        """
        today = datetime.now()
        days_since_monday = today.weekday()
        last_weeks_monday = today - timedelta(days=days_since_monday + 7)
        return last_weeks_monday.strftime("%Y-%m-%d")
