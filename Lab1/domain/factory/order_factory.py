from domain.models.order import Order

class OrderFactory:
    @staticmethod
    def create_order(products):
        return Order(products)