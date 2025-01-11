import pytest

from src.category import Category
from src.product import Product


def test_category_normal(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Овощи"
    assert first_category.description == "Свежие овощи"

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_str(first_category: Category, second_category: Category) -> None:
    """
    Test that the str method of a Category instance returns a string
    containing the name of the category and the total quantity of products
    in the category.

    Parameters:
    ----------
    first_category : Category
        The first category instance to test.
    second_category : Category
        The second category instance to test.
    """
    assert str(first_category) == "Овощи, количество продуктов: 30 шт."
    assert str(second_category) == "Хлеб, количество продуктов: 60 шт."


def test_category_count_increases_when_product_added(
    first_category: Category, second_category: Category, test_product: Product
) -> None:
    """
    Test that the category count increases when a product is added to a category.

    The category count is incremented every time a product is added to a category.
    """
    initial_category_count = Category.category_count
    first_category.add_product(test_product)
    assert Category.category_count == initial_category_count


def test_add_product_raises_type_error() -> None:
    """
    Test that adding a non-Product instance to a Category raises a TypeError.

    This test creates a Category instance and then attempts to add a non-Product
    instance to it. It verifies that a TypeError is raised.
    """
    cat1 = Category("овощи", "любые овощи")
    with pytest.raises(TypeError) as e:
        cat1.add_product("not a product")


def test_product_count_increases_when_product_added(first_category: Category, test_product: Product) -> None:
    """
    Test that the product count increases when a product is added to a category.

    The product count is incremented every time a product is added to a category.
    """
    initial_product_count = Category.product_count
    first_category.add_product(test_product)
    assert Category.product_count == initial_product_count + 1


def test_category_count_does_not_change_when_adding_product_to_empty_category(
    empty_category: Category, test_product: Product
) -> None:
    """
    Test that the category count does not change when a product
    is added to an empty category.

    This test verifies that adding a product to an empty category
    does not increment the overall category count, ensuring that
    the category count remains unchanged.
    """
    initial_category_count = Category.category_count
    empty_category.add_product(test_product)
    assert Category.category_count == initial_category_count


def test_middle_price_normal(first_category: Category) -> None:
    """
    Test that the middle_price method returns the average price of all products
    in a category with a normal number of products.

    This test verifies that the middle_price method returns the correct average
    price of all products in a category with a normal number of products.
    """
    assert first_category.middle_price() == 15.0


def test_middle_price(empty_category: Category) -> None:
    assert empty_category.middle_price() == 0.0


def test_category_add_product_zero_error(capsys: pytest.CaptureFixture, first_category: Category) -> None:
    """
    Test that adding a product with zero quantity to a category
    results in an appropriate error message and does not change
    the product count.

    Parameters:
    ----------
    capsys : pytest.CaptureFixture
        A pytest fixture to capture standard output and error streams.
    first_category : Category
        The category instance to which the product is attempted to be added.

    Returns:
    -------
    None
        This function does not return any value. It asserts the expected
        behavior of the system when a product with zero quantity is added.
    """
    product = Product("Тест", "Количество: 0", 10, 1)
    product.quantity = 0
    first_category.add_product(product)

    message = capsys.readouterr()
    failed, completed = message.out.strip().split("\n")[3:]

    assert Category.product_count == 24
    assert failed == "Невозможно добавить товар с нулевым количеством."
    assert completed == "Обработка добавления товара завершена."
