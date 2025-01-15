import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "Наушники"
    assert first_category.description == "Современные беспроводные наушники"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_products_list_property(first_category):
    assert (
        first_category.products == "AirPods, 35000.0 руб. Остаток: 3 шт.AirPods Pro, 40000.0 руб. Остаток: 2 шт."
    )


def test_category_add_product(second_category, one_product):
    assert len(second_category.products_in_list) == 2
    second_category.add_product(one_product)
    assert len(second_category.products_in_list) == 3

def test_category_str(first_category):
    assert str(first_category) == 'Наушники, количество продуктов: 5 шт.'

def test_products_iterator(products_iterator):
    iter(products_iterator)
    assert products_iterator.index == 0
    assert next(products_iterator).name == "AppleWatch Series 8"
    assert next(products_iterator).name == "AppleWatch Series 9"
    with pytest.raises(StopIteration):
        assert next(products_iterator)
