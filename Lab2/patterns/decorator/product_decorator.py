class ProductDecorator:
    def __init__(self, product):
        self._product = product

    def __str__(self):
        return str(self._product)

class DiscountedProductDecorator(ProductDecorator):
    def __init__(self, product, discount):
        super().__init__(product)
        self.discount = discount

    @property
    def price(self):
        return self._product.price * (1 - self.discount)

    def __str__(self):
        return f"{self._product} - Discounted Price: ${self.price:.2f}"