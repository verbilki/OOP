import pytest

from src.category import Category
from src.products_iterator import ProductIterator


def test_products_iterator_init(products_iterator: ProductIterator, smartphones: Category) -> None:
    """
    Tests that the ProductIterator class is correctly initialized.

    :param products_iterator: The ProductIterator object to test.
    :param smartphones: The Category object to test.
    """
    iterator = products_iterator
    assert iterator.category == smartphones


def test_products_iterator_index(products_iterator: ProductIterator) -> None:
    """
    Test the initial index position of the ProductIterator.

    This test checks that the iterator's initial position is set to -1,
    which indicates that the iterator has not yet started iterating
    over the products.

    Parameters:
    products_iterator (ProductIterator): An instance of ProductIterator to test.

    Returns:
    None: The function asserts the initial position of the iterator.
    """
    assert products_iterator.iter_pos == -1


def test_products_iterator(products_iterator: ProductIterator) -> None:
    """
    Test the ProductIterator class.

    This test checks that the ProductIterator class correctly implements the iterator protocol,
    by checking that the products are yielded in order and that a StopIteration exception
    is raised if the iterator is exhausted.

    Parameters:
    products_iterator (ProductIterator): An instance of ProductIterator to test.

    Returns:
    None: The function asserts the correct behavior of the iterator.
    """
    assert next(products_iterator).name == "Iphone 15"
    assert next(products_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(products_iterator)
