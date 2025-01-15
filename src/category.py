from src.product import Product


class Category:
    """Класс для описания категории продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products
        Category.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Магический метод для отображения информации о количестве продуктов для пользователей"""
        sum_quantity = 0
        for element in self.__products:
            sum_quantity += element.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    def add_product(self, new_product: Product) -> None:
        """Метод для добавления нового продукта"""
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products_in_list(self) -> list:
        return self.__products

    @property
    def products(self) -> str:
        """Метод-геттер для получения строки, содержащей информацию о продуктах категории"""
        product_str = ""
        for element in self.__products:
            product_str += str(element)
        return product_str
