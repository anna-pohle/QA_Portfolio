import uuid

class AuthData:
    EXISTING_USER = {"email":"test16@web.de", "password":"test16"}
    INVALID_USER = {"email":"test16@web.de", "password":"test23"}

    @staticmethod
    def NEW_USER() -> dict:
        #generiert bei jedem Zugriff neue Userdaten
        unique_id = str(uuid.uuid4())[:8]  # Erste 8 Ziffern aus dem aktuellen timestamp
        return {"email":f"testuser_{unique_id}@web.de", "password":"pommes12", "name":"didi"}


class CheckoutData:
    #Testdaten für Checkout
    VALID_ADDRESS = {
        "street": "Hauptstraße 123",
        "city": "Leipzig",
        "postal_code": "04103"
    }

    VALID_PAYMENT = {
        "card_number": "4111111111111111",  # Test-Kreditkarte
        "name_on_card": "Max Mustermann",
        "expiration": "12/2025",
        "cvv": "123"
    }

    # Alternative Testdaten für verschiedene Szenarien
    INVALID_CARD = {
        "card_number": "1234",
        "name_on_card": "Test User",
        "expiration": "01/2020",  # Abgelaufen
        "cvv": "999"
    }