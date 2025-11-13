from pathlib import Path
from typing import Dict, Any

import yaml


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
