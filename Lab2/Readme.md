# Shopping Cart Project - Structural Design Patterns

## Overview
This project implements a shopping cart system using **Structural Design Patterns**. The shopping cart allows for product management, including adding, removing, and viewing items, as well as creating orders. The design emphasizes modularity, flexibility, and the ability to compose objects in different ways to form larger structures.

## Features

- **Product Management**: Create and manage products in the shopping cart.
- **External Product Integration**: Adapt external product data formats to internal models.
- **Dynamic Product Enhancement**: Add features like discounts to products at runtime.
- **Access Control**: Control and track access to product objects.
- **Simplified Interface**: Unified interface for complex shopping operations.
- **Order Creation**: Ability to create orders from the products in the shopping cart.

## Structural Design Patterns

This project employs the following structural design patterns:

### 1. **Adapter Pattern**
The Adapter pattern allows incompatible interfaces to work together. In this project, `ExternalProductAdapter` converts external product data (with different field names like `title`, `cost`, `info`) to our internal `Product` model (with `name`, `price`, `description`).

**Location**: `patterns/adapter/external_product_adapter.py`

**Example**:
```python
external_data = {
    "title": "Smartphone",
    "cost": 599.99,
    "info": "A high-end smartphone.",
    "date": "01/11/2024"
}
adapter = ExternalProductAdapter(external_data)
product = adapter.to_product()  # Converts to internal Product format
```

**Benefits**:
- Allows integration with external systems without modifying existing code
- Maintains separation of concerns
- Makes the system more flexible and extensible

### 2. **Decorator Pattern**
The Decorator pattern allows adding new functionality to objects dynamically without modifying their structure. `DiscountedProductDecorator` wraps a `Product` and adds discount functionality while maintaining the same interface.

**Location**: `patterns/decorator/product_decorator.py`

**Example**:
```python
base_product = Product("Headphones", 199.99, "Noise-canceling headphones")
discounted_product = DiscountedProductDecorator(base_product, 0.20)  # 20% discount
# discounted_product.price returns the discounted price
```

**Benefits**:
- Adds functionality at runtime without modifying the original class
- Follows the Open/Closed Principle
- Allows multiple decorators to be stacked
- Maintains object identity and interface

### 3. **Proxy Pattern**
The Proxy pattern provides a surrogate or placeholder for another object to control access to it. `ProductProxy` wraps a `Product` and can track access, implement lazy loading, or add access control.

**Location**: `patterns/proxy/product_proxy.py`

**Example**:
```python
product = Product("Laptop", 999.99, "A powerful laptop")
proxied_product = ProductProxy(product, access_level="public")
# Access is tracked and can be controlled
access_count = proxied_product.get_access_count()
```

**Benefits**:
- Controls access to the original object
- Can implement lazy loading or caching
- Adds additional functionality without modifying the original object
- Can implement access control and security checks

### 4. **Facade Pattern**
The Facade pattern provides a simplified interface to a complex subsystem, hiding its complexity from the client. `ShoppingFacade` provides a unified interface for all shopping operations, hiding the complexity of the underlying `ShoppingCartClient` and various patterns.

**Location**: `patterns/facade/shopping_facade.py`

**Example**:
```python
facade = ShoppingFacade()
facade.add_product("Gaming Mouse", 79.99, "RGB gaming mouse", "10/11/2024")
facade.add_discounted_product("Keyboard", 149.99, 15, "Mechanical keyboard", "12/11/2024")
facade.view_cart()
facade.create_order("express")
```

**Benefits**:
- Simplifies complex subsystem interactions
- Reduces coupling between client and subsystem
- Provides a single entry point for common operations
- Makes the system easier to use and understand

## Class Structure

### Domain Models
- **Product**: Represents an individual product with attributes such as name, price, description, and date.
- **ShoppingCart**: Manages the list of products added to the cart (uses Singleton pattern for single instance).
- **Order**: Represents an order consisting of products, calculating the total price with shipping options.

### Structural Pattern Implementations
- **ExternalProductAdapter**: Adapts external product data format to internal Product model.
- **ProductDecorator**: Base decorator class for Product objects.
- **DiscountedProductDecorator**: Decorator that adds discount functionality to products.
- **ProductProxy**: Proxy that controls and tracks access to Product objects.
- **ShoppingFacade**: Simplified interface for complex shopping operations.

### Client
- **ShoppingCartClient**: Interacts with the shopping cart, allowing users to add, remove, and view products as well as create orders. Uses various structural patterns internally.

## Pattern Relationships

The patterns work together to create a flexible and extensible system:

1. **Adapter** integrates external data sources
2. **Decorator** enhances products with additional features
3. **Proxy** controls access to products
4. **Facade** provides a simple interface that uses all the above patterns internally

## Usage

To run the shopping cart application and see all structural patterns in action:

```bash
python main.py
```

The demo will showcase:
1. Adapter pattern converting external product data
2. Decorator pattern adding discounts to products
3. Proxy pattern controlling product access
4. Facade pattern simplifying the shopping workflow

## Conclusion

This shopping cart project showcases the effective use of **Structural Design Patterns** to create a modular, flexible, and extensible system. The Adapter pattern enables integration with external systems, the Decorator pattern allows dynamic feature addition, the Proxy pattern provides access control, and the Facade pattern simplifies complex operations. Together, these patterns create a robust foundation for a flexible e-commerce solution that can easily accommodate future requirements and changes.
