import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json_file(path: str) -> Any:
    """Функция читает данные из json файла"""
    try:
        full_path = os.path.abspath(path)
        with open(full_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return {}
    except FileNotFoundError:
        print("There is no such file")
        return {}


def create_object_from_json(data: dict) -> list:
    """Функция преобразует данные из json файла в объекты"""
    if data:
        categories = []
        for category in data:
            products = []
            for product in category["products"]:
                products.append(Product(**product))
            category["products"] = products
            categories.append(Category(**category))
        return categories
    else:
        return []


#
# if __name__ == '__main__':
#     categories_from_json = read_json_file('../data/products.json')
#     categories_object = create_object_from_json(categories_from_json)
#     print(categories_object[1].products)
