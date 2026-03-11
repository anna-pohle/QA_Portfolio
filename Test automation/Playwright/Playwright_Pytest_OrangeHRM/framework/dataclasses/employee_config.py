"""
Employee configuration for test employee creation.

Defines reusable presets for different employee types.
"""
from dataclasses import dataclass


@dataclass
class EmployeePreset:
    """
    Predefined employee configuration for PIM creation.

    Usage:
        # In fixture:
        employee = add_employee_page.create_employee(
            QA_PRESET.name_prefix + "_" + unique_id,
            QA_PRESET.last_name_prefix
        )

        # Or custom preset:
        custom = EmployeePreset(
            name_prefix="Custom",
            last_name_prefix="User"
        )
    """
    name_prefix: str
    last_name_prefix: str = "Test"


# =============================================================================
# PREDEFINED PRESETS
# =============================================================================

# QA Engineer: Standard test employee
QA_PRESET = EmployeePreset(
    name_prefix="E2E_QA",
    last_name_prefix="Tester",
)

# Developer: Alternative preset
DEV_PRESET = EmployeePreset(
    name_prefix="E2E_Dev",
    last_name_prefix="Developer",
)

# Manager: For leave assignment scenarios
MANAGER_PRESET = EmployeePreset(
    name_prefix="E2E_Manager",
    last_name_prefix="Lead",
)
