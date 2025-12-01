from client.shopping_cart_client import ShoppingCartClient

class ShoppingFacade:
    """
    Facade pattern: Provides a simplified interface to the complex
    shopping cart subsystem, hiding the complexity of individual components.
    """
    def __init__(self):
        self.client = ShoppingCartClient()

    def add_product(self, name, price, description=None, date=None):
        """Simplified method to add a product."""
        self.client.add_product(name, price, date, description)

    def add_external_product(self, external_data):
        """Simplified method to add an external product (uses Adapter internally)."""
        self.client.add_external_product(external_data)

    def add_discounted_product(self, name, price, discount_percentage, description=None, date=None):
        """Simplified method to add a discounted product (uses Decorator internally)."""
        self.client.add_discounted_product(name, price, discount_percentage, date, description)

    def view_cart(self):
        """Simplified method to view cart contents."""
        self.client.view_cart()

    def create_order(self, shipping_type="standard"):
        """Simplified method to create an order."""
        return self.client.create_order(shipping_type)

    def clear_cart(self):
        """Simplified method to clear the cart."""
        self.client.clear_cart()