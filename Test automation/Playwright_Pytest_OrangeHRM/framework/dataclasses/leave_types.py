from enum import Enum


class LeaveType(Enum):
    """
    Leave types available in the OrangeHRM demo.

    The value corresponds to the dropdown option text in the UI.
    """
    CAN_VACATION = "CAN - Vacation"
    CAN_PERSONAL = "CAN - Personal"
    CAN_BEREAVEMENT = "CAN - Bereavement"
    CAN_FMLA = "CAN - FMLA"
    US_VACATION = "US - Vacation"
    US_PERSONAL = "US - Personal"


class LeaveStatus(Enum):
    """
    Leave request statuses.

    The value corresponds to the status text displayed in the Leave List table.
    """
    PENDING = "Pending Approval"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"
    SCHEDULED = "Scheduled"
