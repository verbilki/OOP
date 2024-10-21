import pytest

from src.category import Category
from src.product import Product


def test_category(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Овощи"
    assert first_category.description == "Свежие овощи"

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_str(first_category: Category, second_category: Category) -> None:
    assert str(first_category) == "Овощи, количество продуктов: 30 шт."
    assert str(second_category) == "Хлеб, количество продуктов: 60 шт."


def test_category_count_increases_when_product_added(
    first_category: Category, second_category: Category, test_product: Product
) -> None:
    initial_category_count = Category.category_count
    first_category.add_product(test_product)
    assert Category.category_count == initial_category_count


def test_add_product_raises_type_error() -> None:
    cat1 = Category("овощи", "любые овощи")
    with pytest.raises(TypeError) as e:
        cat1.add_product("not a product")
    assert str(e.value) == "Товар должен быть типа Product."


def test_product_count_increases_when_product_added(first_category: Category, test_product: Product) -> None:
    initial_product_count = Category.product_count
    first_category.add_product(test_product)
    assert Category.product_count == initial_product_count + 1


def test_category_count_does_not_change_when_adding_product_to_empty_category(
    empty_category: Category, test_product: Product
) -> None:
    initial_category_count = Category.category_count
    empty_category.add_product(test_product)
    assert Category.category_count == initial_category_count


# def test_category_count_decreases_when_product_removed(first_category, test_product):
#     initial_category_count = Category.category_count
#     first_category.add_product(test_product)
#     assert Category.category_count == initial_category_count
#     first_category.remove_product(test_product)
#     assert Category.category_count == initial_category_count


# def test_product_count_decreases_when_product_removed(first_category, test_product):
#     initial_product_count = Category.product_count
#     first_category.add_product(test_product)
#     assert Category.product_count == initial_product_count + 1
#     first_category.remove_product(test_product)
#     assert Category.product_count == initial_product_count


# def test_category_count_does_not_change_when_removing_product_from_empty_category(empty_category, test_product):
#     initial_category_count = Category.category_count
#     empty_category.remove_product(test_product)
#     assert Category.category_count == initial_category_count


# def test_product_count_does_not_change_when_removing_product_from_empty_category(empty_category, test_product):
#     initial_product_count = Category.product_count
#     empty_category.remove_product(test_product)
#     assert Category.product_count == initial_product_count
