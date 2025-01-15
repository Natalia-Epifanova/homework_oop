import pytest

from src.category import Category
from src.product import Product
from src.products_iterator import ProductsIterator


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


@pytest.fixture()
def one_product():
    return Product(name="AppleWatch Series 10", description="pink", price=56000.0, quantity=3)


@pytest.fixture()
def data_for_test():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        }
    ]


@pytest.fixture()
def products_iterator(second_category):
    return ProductsIterator(second_category)