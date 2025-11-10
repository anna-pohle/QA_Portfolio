from dataclasses import dataclass
from framework.utils import FileUtils

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

    @classmethod
    def from_config(cls, config_key: str) -> 'PaymentCard':
        """
        Holt Daten aus YAML und macht daraus ein User-Objekt
        """
        # 1. Liest die YAML-Datei → gibt ein Dict zurück
        yaml_dict = FileUtils.read_yaml("checkout_data.yaml")

        # 2. Hole die richtigen Daten raus
        payment_data = yaml_dict[config_key]  # z.B. yaml_dict['existing_user']

        # 3. Erstelle User-Objekt mit diesen Daten
        return cls(**payment_data)  # ** entpackt das Dict