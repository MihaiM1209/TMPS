# Shopping Cart Project

## Overview
This project implements a simple shopping cart system using **Creational Design Patterns**. The shopping cart allows for product management, including adding, removing, and viewing items, as well as creating orders. The design emphasizes modularity and scalability, making it easy to extend functionality in the future.

## Features

- **Product Management**: Create and manage products in the shopping cart.
- **Shopping Cart**: A singleton shopping cart that ensures only one instance is available.
- **Order Creation**: Ability to create orders from the products in the shopping cart.
- **Dynamic Interaction**: Users can add new products, view the cart, remove items, and create orders.

## Creational Design Patterns

This project employs the following creational design patterns:

1. **Singleton Pattern**:
   - The `ShoppingCart` class uses the Singleton pattern to ensure that only one instance of the shopping cart exists throughout the application. This prevents multiple carts from being created inadvertently, which could lead to inconsistent states.

   ```python
   class ShoppingCart:

      # PRIVATE INSTANCE CREATION
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.items = []
        return cls._instance
   ```

2. **Factory Method Pattern**:
   - The `OrderFactory` class implements the Factory Method pattern to create `Order` instances. This allows for the encapsulation of the order creation logic, making it easier to manage and extend in the future without changing the existing codebase.
   ```python
   class Order:
    def __init__(self, products):
        self.products = products
        self.total = sum(product.price for product in products)

    def __str__(self):
        product_list = ', '.join(str(product) for product in self.products)
        return f"Order: {product_list}, Total: ${self.total:.2f}"

      class Order:
    def __init__(self, products):
        self.products = products
        self.total = sum(product.price for product in products)

    def __str__(self):
        product_list = ', '.join(str(product) for product in self.products)
        return f"Order: {product_list}, Total: ${self.total:.2f}"

   ```

3. **Builder Pattern**:
   - The Builder pattern could be applied if more complex product creation logic is required, such as creating products with multiple attributes or configurations.

   ```python
   class Product:
    def __init__(self, name, price, description=None):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description or 'No description'}"

   class ProductBuilder:
    def __init__(self):
        self.name = None
        self.price = None
        self.description = None  
   ```

## Class Structure

- **Product**: Represents an individual product with attributes such as name, price, and description.
- **ShoppingCart**: Implements the Singleton pattern, managing the list of products added to the cart.
- **Order**: Represents an order consisting of products, calculating the total price.
- **OrderFactory**: Factory class for creating `Order` instances.
- **ShoppingCartClient**: Interacts with the shopping cart, allowing users to add, remove, and view products as well as create orders.

## Conclustion
   This shopping cart project showcases the effective use of Creational Design Patterns to create a modular, scalable system. The Singleton pattern ensures a single cart instance, while the Factory Method and Builder patterns streamline object creation and allow for easy future extensions. With this design, the project is well-prepared for additional features and adjustments, providing a strong foundation for a flexible e-commerce solution.

## Usage

To run the shopping cart application, execute the `main.py` file:

```bash
python main.py
