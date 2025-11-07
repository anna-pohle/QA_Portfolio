from dataclasses import dataclass
from typing import Optional
from framework.utils import StringUtils


@dataclass
class User:
    #User-Datenmodell für Authentication
    email: str
    password: str
    name: Optional[str] = None

    @classmethod
    def generate_new_user(cls) -> 'User':
        #nutzt die utils, um einen neuen User mit eindeutiger Email zu erstellen
        unique_email = StringUtils.generate_unique_email()
        unique_username = StringUtils.generate_random_string()
        return cls(
            email=unique_email,
            password="SecurePass123",
            name=unique_username
        )


