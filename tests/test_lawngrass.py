import pytest

from src.lawngrass import LawnGrass


def test_create_lawngrass_with_valid_strings() -> None:
    lawn_grass = LawnGrass(
        name="Premium Lawn Grass",
        description="High-quality lawn grass seed",
        price=29.99,
        quantity=100,
        country="USA",
        germination_period="7-10 days",
        color="Green",
    )
    assert lawn_grass.name == "Premium Lawn Grass"
    assert lawn_grass.description == "High-quality lawn grass seed"
    assert lawn_grass.price == 29.99
    assert lawn_grass.quantity == 100
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "7-10 days"
    assert lawn_grass.color == "Green"


def test_create_lawngrass_with_empty_germination_period() -> None:
    lawn_grass = LawnGrass(
        name="Basic Lawn Grass",
        description="Affordable lawn grass seed",
        price=19.99,
        quantity=50,
        country="Canada",
        germination_period="",
        color="Light Green",
    )
    assert lawn_grass.name == "Basic Lawn Grass"
    assert lawn_grass.description == "Affordable lawn grass seed"
    assert lawn_grass.price == 19.99
    assert lawn_grass.quantity == 50
    assert lawn_grass.country == "Canada"
    assert lawn_grass.germination_period == ""
    assert lawn_grass.color == "Light Green"


def test_lawngrass_inherits_product_properties() -> None:
    lawn_grass = LawnGrass(
        name="Eco Lawn Grass",
        description="Eco-friendly lawn grass seed",
        price=2500,
        quantity=75,
        country="Australia",
        germination_period="5-8 days",
        color="Dark Green",
    )
    assert lawn_grass.name == "Eco Lawn Grass"
    assert lawn_grass.description == "Eco-friendly lawn grass seed"
    assert lawn_grass.price == 2500
    assert lawn_grass.quantity == 75


def test_add_lawngrass_and_smartphone_raises_exception(
    lawn_grass_test1: LawnGrass, smartphone_test1: LawnGrass
) -> None:
    with pytest.raises(TypeError):
        _ = lawn_grass_test1 + smartphone_test1


def test_add_smartphone_and_integer_raises_exception(lawn_grass_test1: LawnGrass) -> None:
    with pytest.raises(TypeError):
        _ = lawn_grass_test1 + 1
