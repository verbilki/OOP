class ProductException(Exception):
    """Класс исключения при некорректном количестве объектов класса Product."""

    def __init__(self, *args, **kwargs) -> None:
        self.message = args[0] if args else "Невозможно добавить товар с нулевым количеством."

    def __str__(self) -> str:
        return self.message
