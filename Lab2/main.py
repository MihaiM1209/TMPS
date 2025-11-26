from client.shopping_cart_client import ShoppingCartClient
from patterns.adapter.external_product_adapter import ExternalProductAdapter
from patterns.decorator.product_decorator import DiscountedProductDecorator
from domain.models.product import ProductBuilder

def main():
    client = ShoppingCartClient()

    client.add_product("Laptop", 999.99, "27/10/2024", "A powerful laptop.")

    external_product_data = {
        "title": "Smartphone",
        "cost": 599.99,
        "info": "A high-end smartphone.",
        "date": "01/11/2024"
    }
    adapter = ExternalProductAdapter(external_product_data)
    external_product = adapter.to_product()
    client.cart.add_item(external_product)
    print(f"Added external product {external_product} to the cart.")

    product = ProductBuilder().set_name("Headphones").set_price(199.99).set_description("Noise-canceling headphones.").set_date("05/11/2024").build()
    discounted_product = DiscountedProductDecorator(product, 0.20)
    client.cart.add_item(discounted_product)
    print(f"Added discounted product {discounted_product} to the cart.")

    client.view_cart()
    client.create_order()

    client.clear_cart()
    client.view_cart()

if __name__ == "__main__":
    main()