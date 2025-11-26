from abc import ABC, abstractmethod
import json


# --- S: Single Responsibility Principle ---
# Product only holds and manages product data.
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


# --- O: Open/Closed Principle ---
# --- L: Liskov Substitution Principle ---
# Abstract base class for all printer types.
class Printer(ABC):
    @abstractmethod
    def print_product(self, product: Product):
        pass


# Text printer — prints product details in plain text.
class TextProductPrinter(Printer):
    def print_product(self, product: Product):
        print(f"Product: {product.get_name()}, Price: {product.get_price()} MDL")


# JSON printer — prints product details in JSON format.
class JSONProductPrinter(Printer):
    def print_product(self, product: Product):
        product_data = {
            "name": product.get_name(),
            "price": product.get_price()
        }
        print(json.dumps(product_data, indent=4))


# --- Main Program ---
if __name__ == "__main__":
    # Create products
    product1 = Product("Smartphone", 5000)
    product2 = Product("Laptop", 15000)

    # Use Text Printer
    text_printer = TextProductPrinter()
    text_printer.print_product(product1)
    text_printer.print_product(product2)

    print("\n--- Now printing in JSON format ---\n")

    # Use JSON Printer
    json_printer = JSONProductPrinter()
    json_printer.print_product(product1)
    json_printer.print_product(product2)


