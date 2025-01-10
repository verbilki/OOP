from src.order import Order
from src.smartphone import Smartphone


def test_order_init(smartphone_test1: Smartphone) -> None:
    """
    Test the initialization of the Order class.

    This test verifies that the Order class is correctly initialized with a given product and quantity.
    It checks that the order's product price, name, and description match the product's attributes,
    and that the order's quantity and total order amount are correctly calculated.

    Parameters:
    smartphone_test1 (Smartphone): An instance of the Smartphone class used to create an Order.

    Returns:
    None: The function asserts the correctness of the Order's initialization.
    """
    order1 = Order(smartphone_test1, 3)

    assert order1.product.price == smartphone_test1.price
    assert order1.name == smartphone_test1.name
    assert order1.description == smartphone_test1.description
    assert order1.quantity == 3
    assert order1.order_amt == 240_000


def test_order_str(smartphone_test1: Smartphone) -> None:
    """
    Test the __str__ method of the Order class.

    This test checks that the __str__ method of the Order class returns the correct string representation
    of the order, including the product name, quantity, description, and total amount.

    Parameters:
    smartphone_test1 (Smartphone): An instance of the Smartphone class used to create an Order.

    Returns:
    None: The function asserts the result of the __str__ method against a pre-defined string.
    """
    # Create an order with the specified smartphone and quantity
    order1 = Order(smartphone_test1, 2)

    # Assert that the string representation of the order is correct
    assert (
        str(order1) == "Заказано: Galaxy S21, 2 шт.\n"
        "Описание товара: Latest Samsung smartphone with high performance\n"
        "Итого: 160000 руб."
    )
