"""
Leave test scenarios as Python dataclasses.

Each scenario defines preconditions and expected leave entries.
Replaces hardcoded test data with type-safe Python objects.
"""
from dataclasses import dataclass, field
from typing import List, Optional

from framework.dataclasses.leave_types import LeaveType, LeaveStatus


@dataclass
class LeaveEntry:
    """A single expected leave entry."""
    date_from: str
    date_to: str
    leave_type: LeaveType
    expected_status: LeaveStatus

    def as_tuple(self) -> tuple:
        """For pytest compatibility: (from, to, LeaveType, LeaveStatus)."""
        return (self.date_from, self.date_to, self.leave_type, self.expected_status)


@dataclass
class LeaveScenario:
    """
    A complete leave test scenario.

    Combines preconditions with expected results.
    """
    scenario_id: str
    employee_name: str
    leave_entries: List[LeaveEntry]
    xfail_reason: Optional[str] = None  # If set: mark test as xfail

    @property
    def entries_as_tuples(self) -> List[tuple]:
        """For pytest compatibility."""
        return [e.as_tuple() for e in self.leave_entries]


# =============================================================================
# PREDEFINED SCENARIOS
# =============================================================================

SINGLE_DAY_VACATION = LeaveScenario(
    scenario_id="single_day_vacation",
    employee_name="",  # Set dynamically in test
    leave_entries=[
        LeaveEntry(
            date_from="",  # Set dynamically
            date_to="",    # Set dynamically
            leave_type=LeaveType.CAN_VACATION,
            expected_status=LeaveStatus.SCHEDULED,
        ),
    ],
)

MULTI_DAY_PERSONAL = LeaveScenario(
    scenario_id="multi_day_personal",
    employee_name="",  # Set dynamically in test
    leave_entries=[
        LeaveEntry(
            date_from="",  # Set dynamically
            date_to="",    # Set dynamically
            leave_type=LeaveType.CAN_PERSONAL,
            expected_status=LeaveStatus.SCHEDULED,
        ),
    ],
)


# All scenarios for parametrized tests
ALL_SCENARIOS = [SINGLE_DAY_VACATION, MULTI_DAY_PERSONAL]
