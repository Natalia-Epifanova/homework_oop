from unittest.mock import mock_open, patch

from src.utils import create_object_from_json, read_json_file


@patch("builtins.open", new_callable=mock_open, read_data='{"name": "Смартфоны"}')
def test_read_json_file(mock_file):
    test_data = read_json_file("data/products.json")
    assert test_data == {"name": "Смартфоны"}


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_json_file_empty_file(mock_file):
    test_data = read_json_file("data/products.json")
    assert test_data == {}


@patch("builtins.open", new_callable=mock_open, read_data='("some_string", [4, 5], 3)')
def test_read_json_file_wrong_type_of_data(mock_file):
    test_data = read_json_file("data/products.json")
    assert test_data == {}


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_json_file_file_not_found(mock_file):
    test_data = read_json_file("data/test.json")
    assert test_data == {}


def test_create_object_from_json(data_for_test):
    result = create_object_from_json(data_for_test)
    assert result[0].name == "Смартфоны"
    assert (
        result[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )


def test_create_object_from_json_empty_data():
    result = create_object_from_json({})
    assert result == []
