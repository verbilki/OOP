import pytest

from src.category import Category
from src.product import Product


def test_category(first_category, second_category):
    assert first_category.name == "Овощи"
    assert first_category.description == "Свежие овощи"
    assert len(first_category.products_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_add_product(first_category: Category, first_product: Product):
    assert len(first_category.products_list) == 2
    a = first_category.product_count
    first_category.add_product(first_product)
    assert len(first_category.products_list) == 3
    b = first_category.product_count
    assert (b - a) == 1


def test_products_property(first_category: Category, first_product: Product) -> None:
    assert first_category.products == ("Лук, 10.0 руб. Остаток: 10 шт.\n" "Морковь, 20.0 руб. Остаток: 20 шт.")
    first_category.add_product(first_product)
    assert (
        first_category.products == "Лук, 10.0 руб. Остаток: 10 шт.\n"
        "Морковь, 20.0 руб. Остаток: 20 шт.\n"
        "Noname Product, 10.0 руб. Остаток: 10 шт."
    )


def test_category_str(first_category, second_category):
    assert str(first_category) == "Овощи, количество продуктов: 30 шт."
    assert str(second_category) == "Хлеб, количество продуктов: 60 шт."


# def test_product_iterator(product_iterator):
#     iter(product_iterator)
#     assert product_iterator.index == 0
#     assert next(product_iterator).name == "Лук"
#     assert next(product_iterator).name == "Морковь"

# with pytest.raises(StopIteration):
#     next(product_iterator)


def test_add_product_error(first_category):
    with pytest.raises(TypeError):
        first_category.add_product(1)
