from datetime import datetime
from Classes import Transaction
from Helpers import to_decimal, load_json_file, save_json_file


def transaction_to_dict(transaction: Transaction) -> dict:
    """Convertit un objet Transaction en dictionnaire (JSON)."""

    return {
        "date": transaction.date.isoformat(),
        "name": transaction.name,
        "ticker": transaction.ticker,
        "type": transaction.type,
        "quantity": str(transaction.quantity),
        "price": str(transaction.price),
        "fees": str(transaction.fees),
    }


def dict_to_transaction(data: dict) -> Transaction:
    """Convertit un dictionnaire (JSON) en objet Transaction."""

    return Transaction(
        date=datetime.fromisoformat(data["date"]),
        name=data["name"],
        ticker=data["ticker"],
        type=data["type"],
        quantity=to_decimal(data["quantity"]),
        price=to_decimal(data["price"]),
        fees=to_decimal(data["fees"]),
    )


def save_transaction(transaction: Transaction) -> None:
    """Ajoute une transaction au fichier JSON."""

    transactions = load_json_file()

    transactions.append(transaction_to_dict(transaction))

    save_json_file(transactions)


def load_transactions() -> list[Transaction]:
    """Charge et retourne toutes les transactions depuis le fichier JSON."""

    transactions_data = load_json_file()

    result = []
    for transaction in transactions_data:
        result.append(dict_to_transaction(transaction))

    return result