from unittest.mock import MagicMock, patch

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, read_json


@patch("src.utils.json.load")
@patch("src.utils.open")
def test_read_json(mock_open: MagicMock, mock_load: MagicMock, json_data: list[dict]):
    mock_load.return_value = json_data
    assert read_json("test.json") == json_data
    mock_open.assert_called_once_with("test.json", mode="r", encoding="utf-8")


def test_create_obj_from_json(json_data: dict, product_1: Product, product_2: Product) -> None:
    """
    This function tests the create_objects_from_json function by comparing the attributes of the created objects with
    expected values.

    Parameters:
    json_data (dict): A dictionary containing JSON data representing products.
    product_1 (Product): An instance of the Product class representing the first product in the JSON data.
    product_2 (Product): An instance of the Product class representing the second product in the JSON data.

    Returns:
    None. This function is used for testing purposes and does not return any value.
    """
    test_category: Category = create_objects_from_json(json_data)[0]
    assert test_category.name == "Смартфоны"
