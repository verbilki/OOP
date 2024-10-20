import json

from src.category import Category
from src.product import Product


def read_json(file_path: str) -> dict:
    # full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", file_path)
    with open(file_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))

        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    cat_data = read_json("../data/products.json")
    cats = create_objects_from_json(cat_data)
    print(cats[0].description)
