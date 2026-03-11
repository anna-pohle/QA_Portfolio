import random
import string
import time


class StringUtils:
    """
    Utilities for string operations.

    Provides static methods for string generation.
    """

    @staticmethod
    def generate_unique_email(domain: str = "test.com") -> str:
        """
        Generates a unique email address.

        Args:
            domain: Email domain (default: "test.com").

        Returns:
            Unique email address.
        """
        timestamp = int(time.time())
        return f"testuser_{timestamp}@{domain}"

    @staticmethod
    def generate_random_string(length: int = 10) -> str:
        """
        Generates a random alphanumeric string.

        Args:
            length: Desired length (default: 10).

        Returns:
            Random string.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
