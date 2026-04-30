from decimal import Decimal
import json
from pathlib import Path
from Config import TRANSACTIONS_FILE


def to_decimal(value) -> Decimal:
    return Decimal(str(value))


def load_json_file() -> list:
    if not TRANSACTIONS_FILE.exists():
        return []

    with open(TRANSACTIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json_file(data: list) -> None:
    with open(TRANSACTIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)