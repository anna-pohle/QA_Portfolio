from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    """
    Employee data model for test-created employees.

    Contains all fields returned after creating an employee via PIM.
    Allows type-safe access instead of dict keys.

    Example:
        employee = test_employee  # Fixture returns Employee object
        assign_leave_page.select_employee(employee.full_name)
    """
    # Names
    first_name: str
    last_name: str
    full_name: str  # "FirstName LastName" for UI assertions

    # IDs
    employee_id: str  # Auto-generated or custom Employee ID

    # Optional: Middle name (not always set)
    middle_name: Optional[str] = None
