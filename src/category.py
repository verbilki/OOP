from typing import Any

from src.product import Product


class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        quantity = sum(product.quantity for product in self.__products)
        return f"{self.name.title()}, количество продуктов: {quantity} шт."

    def add_product(self, new_product: Any) -> None:
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError("Товар должен быть типа Product.")

    @property
    def products(self) -> str:
        """
        Property, returning a string representation of all products in the category.

        :return: string representation of all products in the category.
        """
        return "\n".join(str(product) for product in self.__products)


if __name__ == "__main__":
    product1 = Product("огурец", "256GB, Серый цвет, 200MP камера", 1.0, 5)
    product2 = Product("морковь", "512GB, Gray space", 2.0, 8)
    product3 = Product("лук", "1024GB, Синий", 31000.0, 14)
    cat1 = Category("овощи", "любые овощи", [product1, product2])
    # print(cat1.products)
    # cat1.add_product(product1)
    # print(cat1.products)
    # product4.price = 10
    # print(cat1.products)
    # print(cat1)
