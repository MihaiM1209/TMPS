from domain.models.product import Product


class ProductBuilder:
    """Builder pattern for constructing Product objects step by step."""
    
    def __init__(self):
        self._name = None
        self._price = None
        self._description = None
        self._date = None

    def set_name(self, name):
        """Set the product name."""
        self._name = name
        return self

    def set_price(self, price):
        """Set the product price."""
        self._price = price
        return self

    def set_description(self, description):
        """Set the product description."""
        self._description = description
        return self

    def set_date(self, date):
        """Set the product date."""
        self._date = date
        return self

    def build(self):
        """Build and return the final Product object."""
        if self._name is None or self._price is None:
            raise ValueError("Product name and price are required!")
        
        return Product(
            name=self._name,
            price=self._price,
            description=self._description,
            date=self._date
        )