from dataclasses import dataclass

@dataclass
class Address:
    #Adress-Datenmodell für Checkout
    street: str
    city: str
    postal_code: str