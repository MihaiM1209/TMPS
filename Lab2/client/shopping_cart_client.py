from domain.models.shopping_cart import ShoppingCart
from domain.models.product import Product
from domain.models.order import Order
from patterns.adapter.external_product_adapter import ExternalProductAdapter
from patterns.decorator.product_decorator import DiscountedProductDecorator


class ShoppingCartClient:
    def __init__(self):
        self.cart = ShoppingCart()

    def add_product(self, name, price, date=None, description=None):
        product = Product(name, price, description, date)
        self.cart.add_item(product)
        print(f"Added {product} to the cart.")

    def remove_product(self, product):
        if product in self.cart.view_cart():
            self.cart.remove_item(product)
            print(f"Removed {product} from the cart.")
        else:
            print(f"Product not found in the cart.")

    def view_cart(self):
        items = self.cart.view_cart()
        if not items:
            print("  (Cart is empty)")
            return
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item}")
        print(f"\n  Total Price: ${self.cart.total_price():.2f}")

    def create_order(self, shipping_type="standard"):
        if not self.cart.view_cart():
            print("Cart is empty! Cannot create an order.")
            return None
        order = Order(self.cart.view_cart(), shipping_type)
        print(order)
        return order

    def clear_cart(self):
        self.cart.clear_cart()
        print("Shopping cart cleared.")

    def add_external_product(self, external_data):
        adapter = ExternalProductAdapter(external_data)
        product = adapter.to_product()
        self.cart.add_item(product)
        print(f"Added external product {product} to the cart.")

    def add_discounted_product(self, name, price, discount_percentage, date=None, description=None):
        product = Product(name, price, description, date)
        discounted_product = DiscountedProductDecorator(product, discount_percentage / 100.0)
        self.cart.add_item(discounted_product)
        print(f"Added discounted product {discounted_product} to the cart.")