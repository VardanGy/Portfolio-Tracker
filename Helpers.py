from decimal import Decimal
import json
from pathlib import Path
from Config import TRANSACTIONS_FILE


def to_decimal(value) -> Decimal:
    """Convertit une valeur numérique en Decimal."""

    return Decimal(str(value))


def load_json_file() -> list:
    """Lit et retourne le contenu (les transactions) du fichier JSON.
    Retourne une liste vide si le fichier n'existe pas."""

    if not TRANSACTIONS_FILE.exists():
        return []

    with open(TRANSACTIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json_file(data: list) -> None:
    """Écrit la liste de transactions dans le fichier JSON."""

    with open(TRANSACTIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)