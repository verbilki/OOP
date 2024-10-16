# import pytest

# from src.category import Category
# from src.product import Product


def test_category(first_category, second_category):
    assert first_category.name == "Овощи"
    assert first_category.description == "Свежие овощи"

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_str(first_category, second_category):
    assert str(first_category) == "Овощи, количество продуктов: 30 шт."
    assert str(second_category) == "Хлеб, количество продуктов: 60 шт."
