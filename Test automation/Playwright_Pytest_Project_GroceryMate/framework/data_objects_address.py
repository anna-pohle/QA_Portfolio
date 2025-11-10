from dataclasses import dataclass

from framework.utils import FileUtils


@dataclass
class Address:
    #Adress-Datenmodell für Checkout
    street: str
    city: str
    postal_code: str

    @classmethod
    def from_config(cls, config_key: str) -> 'Address':
        """
        Holt Daten aus YAML und macht daraus ein Adress-Objekt
        """
        # 1. Liest die YAML-Datei → gibt ein Dict zurück
        yaml_dict = FileUtils.read_yaml("checkout_data.yaml")

        # 2. Hole die richtigen Daten raus
        address_data = yaml_dict[config_key]  # z.B. yaml_dict['existing_user']

        # 3. Erstelle User-Objekt mit diesen Daten
        return cls(**address_data)  # ** entpackt das Dict