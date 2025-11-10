class StringUtils:
    #Utilities für String-Operationen

    @staticmethod
    def generate_unique_email(domain: str = "test.com") -> str:
        """Generiert einzigartige Email-Adresse"""
        import time
        timestamp = int(time.time())
        return f"testuser_{timestamp}@{domain}"

    @staticmethod
    def generate_random_string(length: int = 10) -> str:
        #Generiert zufälligen String
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
