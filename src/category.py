from typing import Any

from src.baseorder import BaseOrder
from src.product import Product
from src.product_exception import ProductException


class Category(BaseOrder):
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        super().__init__(name, description)
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        quantity = sum(product.quantity for product in self.__products)
        return f"{self.name.title()}, количество продуктов: {quantity} шт."

    def add_product(self, new_product: Any) -> None:
        if isinstance(new_product, Product):
            try:
                if not new_product.quantity:
                    raise ProductException()
            except ProductException as e:
                print(e)
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                print(f"Товар '{new_product.name}' успешно добавлен.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError()

    @property
    def products(self) -> str:
        """
        Property, returning a string representation of all products in the category.

        :return: string representation of all products in the category.
        """
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> list:
        """
        Property, returning a list of all products in the category.

        :return: list of all products in the category.
        """
        return self.__products

    def products_counter(self):
        products_counter = 0
        for product in self.__products:
            products_counter += product.quantity
        return products_counter

    def middle_price(self):
        """
        Method to calculate the average price of all products in the category.

        :return: average price of all products in the category.
        """
        try:
            avg_price = sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0.0
        else:
            return round(avg_price, 2)
        # try:
        #     return sum([prod.price * prod.quantity for prod in self.__products]) / sum(
        #         [prod.quantity for prod in self.__products])
        # except ZeroDivisionError:
        #     return 0


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 1.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 2.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    cat1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
