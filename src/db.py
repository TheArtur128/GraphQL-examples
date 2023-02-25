from dataclasses import dataclass
from decimal import Decimal
from typing import NewType, Final


Dollars = NewType("Dollars", Decimal)


@dataclass
class Product:
    name: str
    description: str
    price: Dollars
    amount: int
