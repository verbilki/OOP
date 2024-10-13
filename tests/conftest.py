import pytest

from src.category import Category
from src.product import Product

# from src.product_iterator import ProductIterator


@pytest.fixture
def first_product() -> Product:
    return Product(name="Noname Product", description="Здесь должно быть описание товара", price=10.0, quantity=10)


@pytest.fixture
def product_dict() -> dict:
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="хлеб",
        description="хлебобулочные изделия",
        products=[
            Product("батон", "батон нарезной", 10.0, 10),
            Product("хлеб", "хлеб бородинский", 20.0, 20),
            Product("хлеб", "хлеб дарницкий", 30.0, 30),
        ],
    )


@pytest.fixture
def product() -> Product:
    return Product("молоко", "молоко ультрапастеризованное 1л", 40.0, 100)


@pytest.fixture
def product_1() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_2() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Овощи",
        description="Свежие овощи",
        products=[Product("Лук", "лук зеленый", 10.0, 10), Product("Морковь", "морковь мытая", 20.0, 20)],
    )


# @pytest.fixture
# def product_iterator(first_category):
#     return ProductIterator(first_category)


@pytest.fixture
def json_data() -> list[dict]:
    """
    This function returns a list of dictionaries representing hierarchical data of products and categories.
    The data is formatted as JSON and is used for testing purposes.

    Returns:
        list[dict]: A list of dictionaries where each dictionary represents a category and its products.
            The dictionary has the following structure:
            {
                "name": str,  # The name of the category
                "description": str,  # The description of the category
                "products": list[dict],  # A list of dictionaries representing products in the category.
            }
    Each product dictionary contains product parameters.
    """
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
    ]
