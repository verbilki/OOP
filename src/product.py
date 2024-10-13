class Product:
    name: str
    description: str
    price: float
    quantity: int
    products: list = []

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Недопустимо добавлять товар с нулевым количеством.")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.products.append(self)

    def __str__(self) -> str:
        return f"{self.name.title()}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError(f"Агрегирование доступно только для объектов класса {self.__class__.__name__}.")

    @classmethod
    def new_product(cls, product: dict) -> "Product":
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
            print("Значение цены не может быть нулевым или отрицательным.")
        elif new_price < self.__price:
            answer = input("Подтвердите снижение стоимости товара (введите y): ")
            if answer.lower().strip() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
