from src.product import Product
from unittest.mock import patch

def test_product_init(product):
    assert product.name == "AirPods"
    assert product.description == "white"
    assert product.price == 35000.0
    assert product.quantity == 3

def test_new_product():
    new_product_test = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product_test.name == "Samsung Galaxy S23 Ultra"
    assert new_product_test.description == "256GB, Серый цвет, 200MP камера"
    assert new_product_test.price == 180000.0
    assert new_product_test.quantity == 5

def test_price_setter(capsys, one_product):
    one_product.price = -3000.0
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"
    one_product.price = 57000.0
    assert one_product.price == 57000.0


@patch("builtins.input")
def test_price_setter_with_user_answer_no(mock_input, one_product):
    mock_input.return_value = 'n'
    one_product.price = 20000.0
    assert one_product.price == 56000.0

@patch("builtins.input")
def test_price_setter_with_user_answer_yes(mock_input, one_product):
    mock_input.return_value = 'y'
    one_product.price = 20000.0
    assert one_product.price == 20000.0