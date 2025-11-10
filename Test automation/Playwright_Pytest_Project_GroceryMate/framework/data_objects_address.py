from dataclasses import dataclass
from framework.utils import FileUtils
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
YAML_PATH = PROJECT_ROOT / "testdata" / "checkout_data.yaml"

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
        yaml_dict = FileUtils.read_yaml(str(YAML_PATH))

        # 2. Hole die richtigen Daten raus
        address_data = yaml_dict[config_key]  # z.B. yaml_dict['existing_user']

        # 3. Erstelle User-Objekt mit diesen Daten
        return cls(**address_data)  # ** entpackt das Dict