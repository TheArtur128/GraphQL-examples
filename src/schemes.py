from typing import Any, Self, Optional

from graphene import ObjectType, NonNull, Int, String, Decimal, Field, Mutation, Boolean, Schema

from db import Product, Dollars, products
from tools import Indexed


class ProductBodyQuery(ObjectType):
    index = NonNull(Int)
    name = NonNull(String)
    description = NonNull(String)
    price = NonNull(Decimal)
    amount = NonNull(Int)

    def resolve_index(indexed_product: Indexed[Product], info: dict) -> int:
        return indexed_product.index

    def resolve_name(indexed_product: Indexed[Product], info: dict) -> str:
        return indexed_product.object_.name

    def resolve_description(indexed_product: Indexed[Product], info: dict) -> str:
        return indexed_product.object_.description

    def resolve_price(indexed_product: Indexed[Product], info: dict) -> Dollars:
        return indexed_product.object_.price

    def resolve_amount(indexed_product: Indexed[Product], info: dict) -> int:
        return indexed_product.object_.amount


class ProductHeadQuery(ObjectType):
    product = Field(ProductBodyQuery, index=NonNull(Int))

    def resolve_product(root: Any, info: dict, index: int):
        return Indexed(products[index], index)

