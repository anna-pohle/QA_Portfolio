from dataclasses import dataclass
from typing import Optional
from framework.utils.StringUtils import StringUtils
from framework.utils.FileUtils import FileUtils
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
YAML_PATH = PROJECT_ROOT / "tests" / "testdata"/ "registration_data.yaml"

@dataclass
class User:
    #User-Datenmodell für Authentication
    email: str
    password: str
    name: Optional[str] = None

    @classmethod
    def from_config(cls, config_key: str) -> 'User':
        """
        Holt Daten aus YAML und macht daraus ein User-Objekt
        """
        # 1. Liest die YAML-Datei → gibt ein Dict zurück
        yaml_dict = FileUtils.read_yaml(str(YAML_PATH))

        # 2. Hole die richtigen Daten raus
        user_data = yaml_dict[config_key]  # z.B. yaml_dict['existing_user']

        # 3. Erstelle User-Objekt mit diesen Daten
        return cls(**user_data)  # ** entpackt das Dict


    @classmethod
    def generate_new_user(cls) -> 'User':
        #nutzt die utils, um einen neuen User mit eindeutiger Email zu erstellen
        unique_email = StringUtils.generate_unique_email()
        unique_username = StringUtils.generate_random_string()
        return cls(
            email=unique_email,
            password="SecurePass123",
            name=unique_username
        )


