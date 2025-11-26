from client.shopping_cart_client import ShoppingCartClient

class ShoppingFacade:
    def __init__(self):
        self.client = ShoppingCartClient()

    def add_product(self, name, price, date=None, description=None):
        self.client.add_product(name, price, date, description)

    def add_external_product(self, external_data):
        self.client.add_external_product(external_data)

    def add_discounted_product(self, name, price, discount, date=None, description=None):
        self.client.add_discounted_product(name, price, discount, date, description)

    def view_cart(self):
        self.client.view_cart()

    def create_order(self):
        self.client.create_order()

    def clear_cart(self):
        self.client.clear_cart()