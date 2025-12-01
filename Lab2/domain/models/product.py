class Product:
    """Product model representing items in the shopping cart."""
    
    def __init__(self, name, price, description=None, date=None):
        self.name = name
        self.price = price
        self.description = description
        self.date = date

    def __str__(self):
        desc = f" - {self.description}" if self.description else ""
        date_info = f" (Date: {self.date})" if self.date else ""
        return f"{self.name}: ${self.price:.2f}{desc}{date_info}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, description='{self.description}', date='{self.date}')"

    def get_price(self):
        """Return the product price."""
        return self.price

    def get_name(self):
        """Return the product name."""
        return self.name

    def get_description(self):
        """Return the product description."""
        return self.description

    def get_date(self):
        """Return the product date."""
        return self.date