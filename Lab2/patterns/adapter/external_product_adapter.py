from domain.models.product import Product
import datetime

class ExternalProductAdapter:
    def __init__(self, external_data):
        self.external_data = external_data

    def to_product(self):
        return Product(
            name=self.external_data['title'],
            price=self.external_data['cost'],
            date=datetime.datetime.now(),
            description=self.external_data.get('info', 'No description')
        )