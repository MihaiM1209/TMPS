

# 🧾 Product Printer Application

## 1. Introduction

This application is built using **object-oriented programming (OOP)** principles, focusing on the `Product` and `Printer` classes to manage products and print their details in different formats.
By leveraging **abstraction** and **inheritance**, the design provides a structured and extensible architecture.
It also demonstrates the application of several **SOLID principles**, promoting robust, scalable, and maintainable software.

---

## 2. Code Overview

### 🧱 Product Class

The `Product` class represents a product with two attributes:

* `name`: name of the product
* `price`: price of the product

It provides getter methods for encapsulation:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
```

This class serves as a simple data container for product details.

---

### 🖨️ Printer Abstract Class

The `Printer` class is an **abstract base class (ABC)** that defines the contract for all printer types.
Every subclass must implement the `print_product` method, which specifies how product details should be displayed.

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_product(self, product):
        pass
```

---

### 🧾 TextProductPrinter Class

A subclass of `Printer` that prints product information in a **plain text** format:

```python
class TextProductPrinter(Printer):
    def print_product(self, product):
        print(f"Product: {product.get_name()}, Price: {product.get_price()} MDL")
```

**Example Output:**

```
Product: Smartphone, Price: 5000 MDL
```

---

### 🧩 JSONProductPrinter Class

Another subclass of `Printer`, this one prints product information in **JSON** format:

```python
import json

class JSONProductPrinter(Printer):
    def print_product(self, product):
        data = {
            "name": product.get_name(),
            "price": product.get_price()
        }
        print(json.dumps(data, indent=4))
```

**Example Output:**

```json
{
    "name": "Smartphone",
    "price": 5000
}
```

---

## 3. Application of SOLID Principles

### 🧠 S — Single Responsibility Principle (SRP)

Each class has one clear responsibility:

* `Product`: stores product data.
* `Printer`: defines the printing interface.
* `TextProductPrinter` and `JSONProductPrinter`: handle specific output formats.

This separation of concerns adheres strictly to SRP.

---

### 🧩 O — Open/Closed Principle (OCP)

The system is **open for extension, closed for modification**.
To add a new format (e.g., XML printer), simply create a new subclass of `Printer` — no need to change existing code.

---

### 🔄 L — Liskov Substitution Principle (LSP)

Any subclass of `Printer` (e.g., `TextProductPrinter`, `JSONProductPrinter`) can replace the base class without affecting correctness.
This works because all subclasses share the same interface (`print_product`).

---

### ⚙️ I — Interface Segregation Principle (ISP)

The abstract class `Printer` defines only the necessary method `print_product`.
The interface remains small and focused, avoiding unnecessary complexity.

---

### 🔌 D — Dependency Inversion Principle (DIP)

The code depends on the abstraction (`Printer`), not concrete implementations.
This makes it easy to inject or replace printers dynamically without modifying client code.

---

## 4. Example Usage and Output

### Example Code

```python
if __name__ == "__main__":
    product1 = Product("Smartphone", 5000)
    product2 = Product("Laptop", 15000)

    text_printer = TextProductPrinter()
    text_printer.print_product(product1)
    text_printer.print_product(product2)

    print("\n--- Now printing in JSON format ---\n")

    json_printer = JSONProductPrinter()
    json_printer.print_product(product1)
    json_printer.print_product(product2)
```

### Example Output

```
Product: Smartphone, Price: 5000 MDL
Product: Laptop, Price: 15000 MDL

--- Now printing in JSON format ---

{
    "name": "Smartphone",
    "price": 5000
}
{
    "name": "Laptop",
    "price": 15000
}
```

---

## 5. Conclusion

This application demonstrates a **clean, maintainable OOP design** guided by the SOLID principles.
By using abstraction and inheritance, new output formats can be added easily without altering existing functionality.
The result is a **modular, extensible, and future-proof** approach to managing and displaying product information.

