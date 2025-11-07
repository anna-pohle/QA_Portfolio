from dataclasses import dataclass

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