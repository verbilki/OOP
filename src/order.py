from src.baseorder import BaseOrder
from src.product import Product
from src.product_exception import ProductException


class Order(BaseOrder):

    def __init__(self, product: Product, quantity: int):
        try:
            if not quantity:
                raise ProductException()
            elif quantity > product.quantity:
                raise ProductException(f"Товар {product.name} доступен в количестве " f"{product.quantity} штук.")
        except ProductException as e:
            print(e)
        else:
            product.quantity -= quantity
            self.product = product
            super().__init__(product.name, product.description)
            self.quantity = quantity
            self.order_amt = self.product.price * self.quantity
            print(f"Товар '{self.name}' успешно добавлен.")
        finally:
            print("Обработка добавления товара в заказ завершена.")

    def __str__(self) -> str:
        return (
            f"Заказано: {self.name}, {self.quantity} шт.\n"
            f"Описание товара: {self.description}\n"
            f"Итого: {round(self.order_amt)} руб."
        )
