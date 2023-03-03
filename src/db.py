from dataclasses import dataclass
from decimal import Decimal
from typing import NewType, Final


Dollars = NewType("Dollars", Decimal)


@dataclass
class Product:
    name: str
    description: str
    price: Dollars
    amount: int = 0


products: Final[list[Product]] = list() # It's a database :D

products.extend([
    Product("Orange", "Very delicious", Dollars(Decimal('5'))),
    Product("Mandarin", "Also very delicious", Dollars(Decimal('3.5'))),
    Product("Stick", "It's a stick", Dollars(Decimal('1')))
])