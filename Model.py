from datetime import datetime
from decimal import Decimal
from Classes import Transaction, Position, PortfolioSituation
from Repository import save_transaction, load_transactions
from Helpers import to_decimal


def buy(date: str, name: str, ticker: str, quantity: float, price: float, fees: float) -> None:
    transaction = Transaction(
        date=datetime.fromisoformat(date),
        name=name.title(),
        ticker=ticker.upper(),
        type="BUY",
        quantity=to_decimal(quantity),
        price=to_decimal(price),
        fees=to_decimal(fees)
    )

    save_transaction(transaction)


def sell(date: str, name: str, ticker: str, quantity: float, price: float, fees: float) -> None:
    situation = build_situation()

    validate_sell(situation, ticker, quantity)

    transaction = Transaction(
        date=datetime.fromisoformat(date),
        name=name.title(),
        ticker=ticker.upper(),
        type="SELL",
        quantity=to_decimal(quantity),
        price=to_decimal(price),
        fees=to_decimal(fees)
    )

    save_transaction(transaction)


def apply_buy(position: Position, transaction) -> None:
    current_cost = (position.quantity * position.average_cost)

    new_cost = (transaction.quantity * transaction.price) + transaction.fees

    total_cost = current_cost + new_cost

    total_quantity = (position.quantity + transaction.quantity)

    position.average_cost = (total_cost / total_quantity)

    position.quantity = total_quantity


def apply_sell(position: Position, transaction) -> None:
    pnl = (transaction.price - position.average_cost) * transaction.quantity

    position.realized_pnl += pnl

    position.quantity -= transaction.quantity


def build_situation() -> PortfolioSituation:
    transactions = load_transactions()

    positions = {}

    for transaction in transactions:
        if transaction.ticker not in positions:
            positions[transaction.ticker] = Position(ticker=transaction.ticker, name=transaction.name)

        position = positions[transaction.ticker]

        if transaction.type == "BUY":
            apply_buy(position, transaction)

        elif transaction.type == "SELL":
            apply_sell(position, transaction)

    active_positions = []

    for position in positions.values():
        if position.quantity > 0:
            active_positions.append(position)

    total_invested = 0

    for position in active_positions:
        total_invested += (position.quantity * position.average_cost)

    return PortfolioSituation(
        positions=active_positions,
        total_positions=len(active_positions),
        total_invested=Decimal(str(total_invested)),
    )


def validate_sell(situation, ticker, quantity):
    for position in situation.positions:

        if position.ticker == ticker:

            if quantity > position.quantity:
                raise ValueError(
                    "Quantité d'actions détenues insuffisante"
                )

            return

    raise ValueError(
        "Valeur non détenue"
    )