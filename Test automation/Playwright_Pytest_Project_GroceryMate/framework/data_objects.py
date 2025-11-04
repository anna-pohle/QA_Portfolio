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
        return cls(
            email=unique_email,
            password="SecurePass123",
            name="Test User"
        )


@dataclass
class Address:
    #Adress-Datenmodell für Checkout
    street: str
    city: str
    postal_code: str


@dataclass
class PaymentCard:
    #Kreditkarten-Datenmodell für Checkout
    card_number: str
    name_on_card: str
    expiration: str
    cvv: str

    def is_valid(self) -> bool:
        #Prüft ob Karte gültig aussieht
        from datetime import datetime
        try:
            exp_date = datetime.strptime(self.expiration, "%m/%Y")
            return exp_date > datetime.now() and len(self.card_number) >= 15
        except:
            return False