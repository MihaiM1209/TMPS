class Order:
    def __init__(self, products):
        self.products = products
        self.total = sum(product.price for product in products)

    def __str__(self):
        product_list = ', '.join(str(product) for product in self.products)
        return f"Order: {product_list}, Total: ${self.total:.2f}"