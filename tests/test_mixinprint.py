import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixinprint_normal(capsys: pytest.CaptureFixture) -> None:
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Iphone 15', '512GB, Gray space', 210000.0, 8)"

    Smartphone("Smartphone1", "Description1", 50_000.0, 5, 98.2, "Model X", 250, "Black")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Smartphone1', 'Description1', 50000.0, 5)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)"
