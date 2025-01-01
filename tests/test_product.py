from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.product import Product


def test_product_init(test_product: Product) -> None:
    assert test_product.name == "молоко"
    assert test_product.description == "молоко ультрапастеризованное 1л"
    assert test_product.price == 40.0
    assert test_product.quantity == 100


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


@pytest.mark.parametrize(
    "invalid_input",
    [
        123,
        {"name": "Laptop"},
        {"description": "A laptop", "name": "Laptop", "price": 1000, "quantity": 0},
    ],
)
def test_new_product_invalid_input(invalid_input) -> None:
    """
    Test the creation of a new Product instance with invalid input.

    This function tests the `new_product` method of the `Product` class by providing invalid input.
    The function is expected to raise a `TypeError` or `ValueError`.

    Parameters:
    invalid_input (various): The input to be used for creating a new Product instance.
                             This can be an integer, a dictionary with missing or incorrect keys, etc.

    Returns:
    None: The function asserts that a `TypeError` or `ValueError` is raised when creating
          a new Product instance with invalid input.
    """
    with pytest.raises((TypeError, ValueError)):
        Product.new_product(invalid_input)


def test_new_product_creation(product_dict: dict) -> None:
    """
    This function tests the creation of a new Product instance using the provided dictionary.

    Parameters:
    product_dict (dict): A dictionary containing the necessary attributes for creating a new Product instance.
                        The dictionary should have the following keys: 'name', 'description', 'price', and 'quantity'.

    Returns: None: The function asserts the attributes of the newly created Product instance
                   against the provided dictionary.
    """
    new_product = Product.new_product(product_dict)
    assert new_product.name == product_dict["name"]
    assert new_product.price == product_dict["price"]
    assert new_product.quantity == product_dict["quantity"]


def test_new_product_update_existing(first_product: Product) -> None:
    """
    This function tests the updating of an existing Product instance with new attributes.

    Parameters:
    first_product (Product): An instance of the Product class representing an existing product.

    Returns:
    None: The function asserts the updated attributes of the Product instance against the provided dictionary.
          It also checks if the quantity of the existing product is correctly updated.
    """
    if first_product is None:
        raise ValueError("first_product is None")
    updated_product = Product.new_product(
        {
            "name": first_product.name,
            "description": first_product.description,
            "price": 15.0,  # Higher price
            "quantity": 5,
        }
    )
    assert updated_product is not None
    assert updated_product.price == 15.0
    assert updated_product.quantity == first_product.quantity + 5


def test_price_setter_wrong_price(product_1: Product, capsys: pytest.CaptureFixture) -> None:
    assert product_1.price == 210000.0
    product_1.price = -210000.0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная.\n"
    product_1.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная.\n"
    assert product_1.price == 210000.0


@patch("builtins.input", return_value="y")
def test_price_setter_lower_price_confirmed(mock_input: MagicMock, product_1: Product):
    assert product_1.price == 210000.0
    product_1.price = 200000.0
    assert product_1.price == 200000.0


@patch("builtins.input", return_value="n")
def test_price_setter_lower_price_not_confirmed(mock_input: MagicMock, product_1: Product):
    assert product_1.price == 210000.0
    product_1.price = 200000.0
    assert product_1.price == 210000.0


def test_product_addition() -> None:
    """
    Test the __add__ method of the Product class.

    This function tests the addition of two Product instances with positive prices and quantities.
    It asserts that the total price calculated by the __add__ method is correct.

    Returns:
    None: The function asserts the result of the __add__ method against the expected total price.
    """
    product1 = Product("Apple", "Fresh apple", 2.0, 10)
    product2 = Product("Banana", "Ripe banana", 1.5, 20)
    total_price = product1 + product2
    assert total_price == (2.0 * 10) + (1.5 * 20)


def test_product_addition_with_zero_price() -> None:
    """
    Test the __add__ method of the Product class when one product has zero price.

    This function tests the addition of two Product instances where one has zero price.
    It asserts that the total price calculated by the __add__ method is correct.

    Returns:
    None: The function asserts the result of the __add__ method against the expected total price.
    """
    product1 = Product("Water", "Bottled water", 0.0, 10)
    product2 = Product("Juice", "Orange juice", 2.5, 5)
    total_price = product1 + product2
    assert total_price == (0.0 * 10) + (2.5 * 5)


def test_product_addition_with_negative_prices() -> None:
    """
    Test the __add__ method of the Product class with negative prices.

    This function tests the addition of two Product instances where both have negative prices
    but positive quantities. It asserts that the total price calculated by the __add__ method
    is correct.

    Returns:
    None: The function asserts the result of the __add__ method against the expected total price.
    """
    product1 = Product("Product A", "Description A", -5.0, 10)
    product2 = Product("Product B", "Description B", -3.0, 20)
    total_price = product1 + product2
    assert total_price == (-5.0 * 10) + (-3.0 * 20)


def test_product_addition_with_different_class() -> None:
    """
    Test the __add__ method of the Product class when adding a Product instance
    to an instance of a different class.

    This function tests the addition of a Product instance with an instance of a
    different class. It asserts that a TypeError is raised.

    Returns:
    None: The function asserts that a TypeError is raised when adding a Product
          instance to an instance of a different class.
    """
    product1 = Product("Laptop", "High-end gaming laptop", 1500.0, 5)
    non_product_instance = "Not a Product instance"
    with pytest.raises(
            TypeError,
            match="Объект Not a Product instance не является экземпляром" " класса <class 'src.product.Product'>.",
    ):
        product1 + non_product_instance


def test_product_addition_with_list() -> None:
    """
    Test the __add__ method of the Product class when adding a Product instance
    to a list.

    This function tests the addition of a Product instance with a list.
    It asserts that a TypeError is raised.

    Returns:
    None: The function asserts that a TypeError is raised when adding a Product
          instance to a list.
    """
    product1 = Product("Laptop", "High-end gaming laptop", 1500.0, 5)
    non_product_instance: list[Any] = []
    with pytest.raises(TypeError, match="Объект \[\] не является экземпляром класса <class 'src.product.Product'>."):
        product1 + non_product_instance
