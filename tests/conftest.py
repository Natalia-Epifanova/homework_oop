import pytest

from src.product import Product
from src.category import Category


@pytest.fixture()
def product():
    return Product(name="AirPods", description="white", price=35000.0, quantity=3)


@pytest.fixture()
def first_category():
    return Category(
        name="Наушники",
        description="Современные беспроводные наушники",
        products=[
            Product(name="AirPods", description="white", price=35000.0, quantity=3),
            Product(name="AirPods Pro", description="white", price=40000.0, quantity=2),
        ],
    )


@pytest.fixture()
def second_category():
    return Category(
        name="Часы",
        description="Умные часы от Apple",
        products=[
            Product(name="AppleWatch Series 8", description="green", price=36000.0, quantity=7),
            Product(name="AppleWatch Series 9", description="blue", price=42000.0, quantity=4),
        ],
    )
