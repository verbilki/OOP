from src.baseorder import BaseOrder
from src.product import Product


class Order(BaseOrder):

    def __init__(self, product: Product, quantity: int):
        super().__init__(product.name, product.description)
        self.product = product
        product.quantity -= quantity
        self.quantity = quantity
        self.order_amt = self.product.price * self.quantity
        print(f"Товар '{self.name}' успешно добавлен.")

    def __str__(self) -> str:
        return (
            f"Заказано: {self.name}, {self.quantity} шт.\n"
            f"Описание товара: {self.description}\n"
            f"Итого: {round(self.order_amt)} руб."
        )
