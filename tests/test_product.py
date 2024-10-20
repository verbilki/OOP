import pytest

from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "молоко"
    assert product.description == "молоко ультрапастеризованное 1л"
    assert product.price == 40.0
    assert product.quantity == 100


def test_product_init_negative_or_zero_price() -> None:
    with pytest.raises(ValueError, match="Значение цены не может быть нулевым или отрицательным."):
        Product("Test Product", "Test Description", -10.0, 10)


def test_product_init_zero_quantity() -> None:
    with pytest.raises(ValueError, match="Недопустимо добавлять товар с нулевым или отрицательным количеством."):
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)


def test_product_str(first_product: Product) -> None:
    """
    Test the __str__ method of the Product class.
    The __str__ method should return a string containing the product name, price, and quantity.

    Parameters:
    first_product (Product): An instance of the Product class used to test its __str__ method.

    Returns:
    None: The function asserts the result of the __str__ method against a pre-defined string.
    """
    assert str(first_product) == "Noname Product, 10.0 руб. Остаток: 10 шт."
