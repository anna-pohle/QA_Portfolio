import uuid

unique_id = str(uuid.uuid4())[:8]  # Erste 8 Ziffern aus dem aktuellen timestamp
test_data = {"email":f"testuser_{unique_id}@web.de", "password":"pommes1", "name":"didi1"}

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