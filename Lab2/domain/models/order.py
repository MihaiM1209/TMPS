class Order:
    def __init__(self, products, shipping_type="standard"):
        self.items = products
        self.order_type = shipping_type
        self.total_price = sum(item.price for item in products)

    def __str__(self):
        lines = [f"Order Details ({self.order_type.upper()} shipping):"]
        lines.append("-" * 60)
        for i, item in enumerate(self.items, 1):
            lines.append(f"  {i}. {item}")
        lines.append("-" * 60)
        lines.append(f"  Total: ${self.total_price:.2f}")
        return "\n".join(lines)