import yaml
from pathlib import Path
from typing import Any, Dict


class FileUtils:
    #Utilities für Datei-Operationen

    @staticmethod
    def read_yaml(file_path: str) -> Dict[str, Any]:
        """
        Liest YAML-Datei und gibt Dictionary zurück
        Args:
            file_path: Pfad zur YAML-Datei
        Returns:
            Dictionary mit YAML-Inhalten
        Raises:
            FileNotFoundError: Wenn Datei nicht existiert
            yaml.YAMLError: Wenn YAML ungültig ist
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"YAML-Datei nicht gefunden: {file_path}")

        with open(path, 'r', encoding='utf-8') as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as e:
                raise yaml.YAMLError(f"Fehler beim Parsen der YAML-Datei: {e}")


class DateUtils:
    #Utilities für Datums-Operationen

    @staticmethod
    def get_date_x_years_ago(years: int) -> str:
        """Gibt Datum vor X Jahren zurück im Format DD-MM-YYYY"""
        from datetime import datetime, timedelta
        date = datetime.now() - timedelta(days=years * 365)
        return date.strftime("%d-%m-%Y")

    @staticmethod
    def get_current_timestamp() -> str:
        #Gibt aktuellen Unix-Timestamp zurück
        import time
        return str(int(time.time()))


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