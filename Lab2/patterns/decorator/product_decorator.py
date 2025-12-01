class ProductDecorator:
    """Base decorator class for Product objects."""
    def __init__(self, product):
        self._product = product

    @property
    def name(self):
        return self._product.name

    @property
    def price(self):
        return self._product.price

    @property
    def description(self):
        return self._product.description

    @property
    def date(self):
        return self._product.date

    def __str__(self):
        return str(self._product)

    def __repr__(self):
        return repr(self._product)


class DiscountedProductDecorator(ProductDecorator):
    """Decorator that adds discount functionality to a product."""
    def __init__(self, product, discount_percentage):
        super().__init__(product)
        self.discount_percentage = discount_percentage  # e.g., 0.20 for 20%

    @property
    def price(self):
        """Calculate discounted price."""
        return self._product.price * (1 - self.discount_percentage)

    def __str__(self):
        original_price = self._product.price
        discounted_price = self.price
        return f"{self._product} - {self.discount_percentage*100:.0f}% Discount: ${discounted_price:.2f} (was ${original_price:.2f})"