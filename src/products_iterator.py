from src.category import Category
from src.product import Product


class ProductIterator:
    category: Category

    def __init__(self, category: Category) -> None:
        """
        Initialize an instance of the ProductIterator class.

        The ProductIterator class implements the iterator protocol and is used to iterate
        over the products in a category.

        Parameters
        ----------
        category : Category
            The category whose products this iterator will iterate over.
        """
        self.category = category

    def __iter__(self):
        """
        Initialize the iterator.

        This method is required by the iterator protocol and is used to initialize
        the iterator.

        Returns:
            The iterator instance itself.
        """
        self.iter_pos = -1
        return self

    def __next__(self) -> Product:
        """
        Returns the next product in the category's product list.

        Returns:
            The next product in the category's product list.

        Raises:
            StopIteration: If there are no more products to iterate over.
        """
        if self.iter_pos + 1 < self.category.product_count:
            self.iter_pos += 1
            return self.category.products_list[self.iter_pos]
        else:
            raise StopIteration
