from typing import Any


class Product:
    """Класс для описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Магический метод для отображения информации о продукте для пользователей"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> Any:
        """Магический метод для сложения стоимости продуктов"""
        return self.__price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, info_product: dict, products_list: list) -> "Product":
        """Метод для добавления нового продукта"""
        existing_product = None
        for element in products_list:
            if element.name == info_product["name"]:
                existing_product = element
                break
        if existing_product:
            cls.quantity = existing_product.quantity + info_product["quantity"]
            cls.__price = max(info_product["price"], existing_product.price)
        else:
            cls.quantity = info_product["quantity"]
            cls.__price = info_product["price"]
        cls.name, cls.description = info_product["name"], info_product["description"]
        return Product(cls.name, cls.description, cls.__price, cls.quantity)

    @property
    def price(self) -> float:
        """Метод-геттер для вывода цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Метод-сеттер для установки новой цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_input = input("Вы уверены, что нужно снизить цену? y/n: ")
            if user_input == "y":
                self.__price = new_price
        elif new_price > self.__price:
            self.__price = new_price
