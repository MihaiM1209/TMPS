from client.shopping_cart_client import ShoppingCartClient
from domain.models.product import Product
from patterns.adapter.external_product_adapter import ExternalProductAdapter
from patterns.decorator.product_decorator import DiscountedProductDecorator
from patterns.facade.shopping_facade import ShoppingFacade
from patterns.proxy.product_proxy import ProductProxy

def main():
    print("=" * 70)
    print("SHOPPING CART SYSTEM - Structural Design Patterns Demo")
    print("=" * 70)
    
    # === PART 1: ADAPTER PATTERN ===
    print("\n" + "=" * 70)
    print("1. ADAPTER PATTERN - Converting External Data to Internal Model")
    print("=" * 70)
    print("\nThe Adapter pattern allows incompatible interfaces to work together.")
    print("Here, we adapt external product data (with different field names)")
    print("to our internal Product model.\n")
    
    client = ShoppingCartClient()
    
    external_product_data = {
        "title": "Smartphone",
        "cost": 599.99,
        "info": "A high-end smartphone with advanced features.",
        "date": "01/11/2024"
    }
    
    print("External product data structure:")
    print(f"  {external_product_data}")
    print("\nUsing Adapter to convert to internal Product model...")
    
    adapter = ExternalProductAdapter(external_product_data)
    adapted_product = adapter.to_product()
    client.cart.add_item(adapted_product)
    print(f"✓ Adapted: {adapted_product.name} - ${adapted_product.price:.2f}")
    print(f"  (title → name, cost → price, info → description)")

    # === PART 2: DECORATOR PATTERN ===
    print("\n" + "=" * 70)
    print("2. DECORATOR PATTERN - Adding Functionality Dynamically")
    print("=" * 70)
    print("\nThe Decorator pattern allows adding new functionality to objects")
    print("dynamically without modifying their structure.\n")
    
    print("Creating a base product...")
    base_product = Product("Headphones", 199.99, "Noise-canceling headphones", "05/11/2024")
    print(f"  Base product: {base_product.name} - ${base_product.price:.2f}")
    
    print("\nApplying Discount Decorator (20% off)...")
    discounted_product = DiscountedProductDecorator(base_product, 0.20)
    client.cart.add_item(discounted_product)
    print(f"✓ Decorated product: {discounted_product}")
    print(f"  Original price: ${base_product.price:.2f}")
    print(f"  Discounted price: ${discounted_product.price:.2f}")
    print(f"  Savings: ${base_product.price - discounted_product.price:.2f}")

    # === PART 3: PROXY PATTERN ===
    print("\n" + "=" * 70)
    print("3. PROXY PATTERN - Controlling Access to Products")
    print("=" * 70)
    print("\nThe Proxy pattern provides a surrogate or placeholder for another")
    print("object to control access to it. Here, we track access to products.\n")
    
    regular_product = Product("Laptop", 999.99, "A powerful laptop", "27/10/2024")
    print(f"Creating product: {regular_product.name} - ${regular_product.price:.2f}")
    
    print("\nWrapping product with Proxy for access control...")
    proxied_product = ProductProxy(regular_product, access_level="public")
    client.cart.add_item(proxied_product)
    print(f"✓ Proxied product: {proxied_product}")
    
    # Demonstrate proxy access tracking
    print("\nAccessing product properties through proxy:")
    _ = proxied_product.name
    _ = proxied_product.price
    _ = proxied_product.description
    print(f"  Product accessed {proxied_product.get_access_count()} times")
    print("  (Proxy can track, cache, or control access to the product)")

    # View cart
    print("\n" + "-" * 70)
    print("CURRENT CART CONTENTS")
    print("-" * 70)
    client.view_cart()
    
    print("\n" + "-" * 70)
    print("CHECKOUT (Standard Shipping)")
    print("-" * 70)
    order = client.create_order("standard")
    if order:
        print(f"\n✓ Order created successfully")
        print(f"✓ Shipping type: {order.order_type.upper()}")
        print(f"✓ Total items: {len(order.items)}")

    # === PART 4: FACADE PATTERN ===
    print("\n\n" + "=" * 70)
    print("4. FACADE PATTERN - Simplified Interface to Complex Subsystem")
    print("=" * 70)
    print("\nThe Facade pattern provides a simplified interface to a complex")
    print("subsystem, hiding its complexity from the client.\n")
    
    facade = ShoppingFacade()
    
    print("Using Facade for simplified shopping operations:\n")
    print("1. Adding regular product via Facade...")
    facade.add_product("Gaming Mouse", 79.99, "RGB gaming mouse", "10/11/2024")
    
    print("\n2. Adding discounted product via Facade (uses Decorator internally)...")
    facade.add_discounted_product("Keyboard", 149.99, 15, "Mechanical keyboard", "12/11/2024")
    
    print("\n3. Adding external product via Facade (uses Adapter internally)...")
    external_data = {
        "title": "Monitor",
        "cost": 399.99,
        "info": "27-inch 4K monitor",
        "date": "15/11/2024"
    }
    facade.add_external_product(external_data)

    print("\n" + "-" * 70)
    print("FACADE CART CONTENTS")
    print("-" * 70)
    facade.view_cart()
    
    print("\n" + "-" * 70)
    print("FACADE CHECKOUT (Express Shipping)")
    print("-" * 70)
    facade_order = facade.create_order("express")
    if facade_order:
        print(f"\n✓ Facade order created successfully")
        print(f"✓ Shipping type: {facade_order.order_type.upper()}")
        print(f"✓ Total items: {len(facade_order.items)}")
    
    # === Summary ===
    print("\n\n" + "=" * 70)
    print("STRUCTURAL DESIGN PATTERNS SUMMARY")
    print("=" * 70)
    print("✓ ADAPTER:   Converted external product data format to internal Product model")
    print("✓ DECORATOR: Added discount functionality to products dynamically")
    print("✓ PROXY:     Controlled and tracked access to product objects")
    print("✓ FACADE:    Simplified complex shopping workflow with unified interface")
    print("=" * 70)
    print("\nAll Structural Design Patterns demonstrated successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()