from typing import Any


class Product:
    name: str
    description: str

    quantity: int
    products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price

        if quantity <= 0:
            raise ValueError("Недопустимо добавлять товар с нулевым или отрицательным количеством.")
        self.quantity = quantity

        self.products.append(self)

    def __str__(self) -> str:
        return f"{self.name.title()}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any):
        """
        Magic method to add two products together.

        This method adds the price of the current instance multiplied by its quantity
        with the price of the other instance multiplied by its quantity.
        The result is the total price of both products.
        If the other instance is not of the same class, a TypeError is raised.

        Parameters:
        ----------
        other: Product
            The other instance to add to the current instance.

        Returns: float
            The total price of the two products.

        Raises: TypeError
            If the other instance is not of the same class.
        """
        if isinstance(other, self.__class__):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError(f"Объект {str(other)} не является экземпляром класса {self.__class__}.")

    @classmethod
    def new_product(cls, product: Any) -> "Product":
        if not isinstance(product, dict):
            raise TypeError("Аргумент product должен быть типа dict.")

        if not all(i in sorted(product.keys()) for i in ["description", "name", "price", "quantity"]):
            raise ValueError("В словаре product должны быть ключи 'description', 'name', 'price', 'quantity'.")

        if any(obj.name == product.get("name") for obj in cls.products):
            for obj in cls.products:
                if obj.name == product.get("name"):
                    if product.get("price") > obj.price:
                        obj.price = product.get("price")
                        obj.quantity += product.get("quantity")
                        return obj

                    else:
                        obj.quantity += product.get("quantity")
                        return obj

        else:
            return cls(**product)

    @property
    def price(self) -> float:
        if self.__price is None:
            raise RuntimeError("Цена не определена.")
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
        elif new_price < self.__price:
            answer = input("Подтвердите снижение стоимости товара (введите y): ")
            if answer.lower().strip() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
