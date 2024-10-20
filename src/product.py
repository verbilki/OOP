class Product:
    name: str
    description: str
    price: float
    quantity: int
    products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description

        if price <= 0.0:
            raise ValueError("Значение цены не может быть нулевым или отрицательным.")
        self.price = price

        if quantity <= 0:
            raise ValueError("Недопустимо добавлять товар с нулевым или отрицательным количеством.")
        self.quantity = quantity

        self.products.append(self)

    def __str__(self) -> str:
        return f"{self.name.title()}, {self.price} руб. Остаток: {self.quantity} шт."
