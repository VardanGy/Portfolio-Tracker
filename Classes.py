from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Transaction:
    date: datetime
    name: str
    ticker: str
    type: str
    quantity: Decimal
    price: Decimal
    fees: Decimal


@dataclass
class Position:
    name: str
    ticker: str
    quantity: Decimal = Decimal("0")
    average_cost: Decimal = Decimal("0")
    realized_pnl: Decimal = Decimal("0")


@dataclass
class PortfolioSituation:
    positions: list[Position]
    total_positions: int
    total_invested: Decimal
