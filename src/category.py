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
            product_str += f"{element.name}, {element.price} руб. Остаток: {element.quantity} шт.\n"
        return product_str
