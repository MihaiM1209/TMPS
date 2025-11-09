class ShoppingCart:
    _instance = None
    #
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.items = []
        return cls._instance

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def view_cart(self):
        return self.items

    def clear_cart(self):
        self.items = []

    def total_price(self):
        return sum(item.price for item in self.items)