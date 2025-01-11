import pytest

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


def test_order_unsufficient_quantity(capsys: pytest.CaptureFixture, smartphone_test1: Smartphone) -> None:
    Order(smartphone_test1, 6)
    message = capsys.readouterr()
    assert message.out.split("\n")[1] == "Товар Galaxy S21 доступен в количестве 5 штук."


def test_order_zero_qnantity(capsys: pytest.CaptureFixture, smartphone_test1: Smartphone) -> None:
    def test_order_init_zero_error(capsys: pytest.CaptureFixture, smartphone_test1: Smartphone) -> None:
        """
        Test the error handling of the Order class when the quantity is zero.

        This test verifies that the Order class correctly handles an attempt to
        create an order with a quantity of zero. It checks that the correct error
        message is printed and the order initialization is completed.

        Parameters:
        capsys (pytest.CaptureFixture): A fixture that captures the output of the
            console.
        smartphone_test1 (Smartphone): An instance of the Smartphone class used
            to create an Order.

        Returns:
        None: The function asserts the correctness of the Order's error handling.
        """
        Order(smartphone_test1, 0)
        message = capsys.readouterr()
        failed, completed = message.out.strip().split("\n")[1:]
        assert failed == "Невозможно добавить товар с нулевым количеством."
        assert completed == "Обработка добавления товара в заказ завершена."


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
    assert str(order1) == (
        "Заказано: Galaxy S21, 2 шт.\n"
        "Описание товара: Latest Samsung smartphone with high performance\nИтого: 160000 руб."
    )
