from domain.models.product import ProductBuilder
from domain.models.shopping_cart import ShoppingCart
from domain.factory.order_factory import OrderFactory

class ShoppingCartClient:
    def __init__(self):
        self.cart = ShoppingCart()

    def add_product(self, name, price, date=None, description=None):
        product = ProductBuilder().set_name(name).set_price(price).set_description(description).set_date(date).build()
        self.cart.add_item(product)
        print(f"Added {product} to the cart.")

    def remove_product(self, product):
        if product in self.cart.view_cart():
            self.cart.remove_item(product)
            print(f"Removed {product} from the cart.")
        else:
            print(f"{product} not found in the cart.")

    def view_cart(self):
        print("Shopping Cart Items:")
        for item in self.cart.view_cart():
            print(item)
        print(f"Total Price: ${self.cart.total_price():.2f}")

    def create_order(self):
        if not self.cart.view_cart():
            print("Cart is empty! Cannot create an order.")
            return
        order = OrderFactory.create_order(self.cart.view_cart())
        print(order)

    def clear_cart(self):
        self.cart.clear_cart()
        print("Shopping cart cleared.")