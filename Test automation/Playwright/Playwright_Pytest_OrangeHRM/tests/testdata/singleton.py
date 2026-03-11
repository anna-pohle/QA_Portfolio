"""
Singleton for session-wide employee instances.

Allows reusing an employee across multiple tests without
recreating it each time. Useful for the session-scoped employee
that is shared across leave and PIM tests.
"""
import logging
from typing import Optional

from framework.dataclasses.data_object_employee import Employee

logger = logging.getLogger(__name__)


class EmployeeSession:
    """
    Singleton class for persistent employee sessions.

    Stores Employee objects and counters that can be reused
    across multiple tests.

    Example:
        session = EmployeeSession()
        if session.primary_employee is None:
            session.primary_employee = create_employee(...)

        # Get next date offset for leave assignment
        days_ahead = session.get_next_future_day()
    """
    _instance: Optional['EmployeeSession'] = None

    # Employee instances
    primary_employee: Optional[Employee] = None
    secondary_employee: Optional[Employee] = None

    # Counters for used days
    _future_days_used: int = 0    # Starts at 1 (tomorrow), counts forward

    def __new__(cls) -> 'EmployeeSession':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_next_future_day(self) -> int:
        """
        Returns the next available day in the future.

        Starts at 1 (tomorrow) and counts up (1, 2, 3, ...).
        Each call returns a new day.

        Returns:
            Offset for DateUtils.get_date_x_days_from_now()
            (1 = tomorrow, 2 = day after, ...)
        """
        self._future_days_used += 1
        logger.info(
            f"[EmployeeSession] Future day #{self._future_days_used} "
            f"claimed (total: {self._future_days_used})"
        )
        return self._future_days_used

    @property
    def future_days_used(self) -> int:
        """Number of future days used so far."""
        return self._future_days_used

    def reset(self) -> None:
        """Resets all employees and counters (for cleanup)."""
        logger.info(
            f"[EmployeeSession] Reset - clearing "
            f"{self._future_days_used} future days"
        )
        self.primary_employee = None
        self.secondary_employee = None
        self._future_days_used = 0
