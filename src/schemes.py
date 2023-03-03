from typing import Any, Self, Optional

from graphene import ObjectType, NonNull, Int, String, Decimal, Field, Mutation, Boolean, Schema
from graphql.execution.execute import ExecutionResult

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


class ProductCreation(Mutation):
    class Arguments:
        name = NonNull(String)
        description = NonNull(String, default_value=str())
        price = NonNull(Decimal)
        amount = NonNull(Int, default_value=0)

    index = NonNull(Int)

    def mutate(root: Any, info: dict, name: str, price: Dollars, description: str, amount: int) -> Self:
        created_product = Product(name, description, price, amount)

        products.append(created_product)

        return ProductCreation(index=len(products) - 1)


class ProductUpdating(Mutation):
    class Arguments:
        name = String()
        description = String()
        price = Decimal()
        amount = Int()

    ok = NonNull(Boolean)

    def mutate(
        product_index: int,
        info: dict,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[Dollars] = None,
        amount: Optional[int] = None,
    ) -> Self:
        product = products[product_index]

        if name is not None:
            product.name = name

        if description is not None:
            product.description = description

        if price is not None:
            product.price = price

        if amount is not None:
            product.amount = amount

        return ProductUpdating(ok=True)


class ProductUpdatingQuery(ObjectType):
    update_product = ProductUpdating.Field()


class ProductDeleting(Mutation):
    class Arguments:
        index = NonNull(Int)

    ok = NonNull(Boolean)

    def mutate(root: Any, info: dict, index: int) -> Self:
        products.pop(index)

        return ProductDeleting(ok=True)


class ProductMutationQuery(ObjectType):
    create_product = ProductCreation.Field()
    delete_product = ProductDeleting.Field()

    product_updating = Field(ProductUpdatingQuery, index=NonNull(Int))

    def resolve_product_updating(root: Any, info: dict, index: int) -> int:
        return index


    return {
        "data": execution_result.data,
        "errors": tuple(map(str, execution_result.errors if execution_result.errors else tuple()))
    }


product_schema = Schema(query=ProductHeadQuery, mutation=ProductMutationQuery)

