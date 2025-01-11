


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

    @classmethod
    def new_product(cls, info_product: dict):
        """Метод для добавления нового продукта"""
        # from src.category import Category
        # products_list = Category.products_in_list
        # print(f'ТИП ДАННЫХ: {type(products_list)}')
        # for product in products_list:
        #     if info_product["name"] in product.name:
        #         quantity = info_product["quantity"] + product.quantity
        #         cls.quantity = quantity
        #     else:
        #         cls.quantity = info_product["quantity"]
        # for product in products_list:
        #     if info_product["name"] == product.name:
        #         max_price = max(info_product["price"], product.price)
        #         cls.__price = max_price
        # cls.name = info_product["name"]
        # cls.description = info_product["description"]
        # cls.quantity = info_product["quantity"]
        # return Product(cls.name, cls.description, cls.quantity, cls.__price)

        return cls(info_product["name"], info_product["description"], info_product["price"], info_product["quantity"])

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


# ДДля данного метода реализуйте проверку наличия такого же товара схожего по имени. В случае если товар уже существует,
# необходимо сложить количество в наличии старого товара и нового. При конфликте цен выбрать ту, которая является более высокой.
# Для этого можно в метод передать список товаров, в котором нужно искать дубликаты.
