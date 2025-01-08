import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_create_smartphone_with_zero_quantity() -> None:
    with pytest.raises(ValueError):
        Smartphone(
            name="Galaxy S21",
            description="Super smartphone",
            price=799.99,
            quantity=0,
            efficiency=0.85,
            model="S21",
            memory=128,
            color="Phantom Gray",
        )


def test_create_smartphone_with_valid_attributes() -> None:
    smartphone = Smartphone(
        name="Galaxy S21",
        description="Latest Samsung smartphone with high performance",
        price=799.99,
        quantity=50,
        efficiency=0.85,
        model="S21",
        memory=128,
        color="Phantom Gray",
    )
    assert smartphone.name == "Galaxy S21"
    assert smartphone.description == "Latest Samsung smartphone with high performance"
    assert smartphone.price == 799.99
    assert smartphone.quantity == 50
    assert smartphone.efficiency == 0.85
    assert smartphone.model == "S21"
    assert smartphone.memory == 128
    assert smartphone.color == "Phantom Gray"


def test_create_smartphone_with_zero_memory() -> None:
    smartphone = Smartphone(
        name="Galaxy S21",
        description="Latest Samsung smartphone with high performance",
        price=799.99,
        quantity=50,
        efficiency=0.85,
        model="S21",
        memory=0,
        color="Phantom Gray",
    )
    assert smartphone.memory == 0


def test_add_smartphone_and_lawngrass_raises_exception(
    smartphone_test1: Smartphone, lawn_grass_test1: LawnGrass
) -> None:
    with pytest.raises(TypeError):
        _ = smartphone_test1 + lawn_grass_test1


def test_add_smartphone_and_integer_raises_exception(smartphone_test1: Smartphone) -> None:
    with pytest.raises(TypeError):
        _ = smartphone_test1 + 1
