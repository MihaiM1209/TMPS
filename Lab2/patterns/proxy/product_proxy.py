from domain.models.product import Product


class ProductProxy:
    """
    Proxy pattern: Controls access to Product objects.
    This proxy can add additional functionality like access control,
    lazy loading, or caching without modifying the original Product class.
    """
    
    def __init__(self, product, access_level="public"):
        self._product = product
        self._access_level = access_level
        self._access_count = 0
    
    @property
    def name(self):
        """Proxy access to product name with access tracking."""
        self._access_count += 1
        return self._product.name
    
    @property
    def price(self):
        """Proxy access to product price with access tracking."""
        self._access_count += 1
        if self._access_level == "restricted":
            # In a real scenario, you might check permissions here
            return None
        return self._product.price
    
    @property
    def description(self):
        """Proxy access to product description."""
        self._access_count += 1
        return self._product.description
    
    @property
    def date(self):
        """Proxy access to product date."""
        self._access_count += 1
        return self._product.date
    
    def get_price(self):
        """Get price through proxy."""
        return self.price
    
    def get_name(self):
        """Get name through proxy."""
        return self.name
    
    def get_description(self):
        """Get description through proxy."""
        return self.description
    
    def get_date(self):
        """Get date through proxy."""
        return self.date
    
    def get_access_count(self):
        """Get the number of times this product was accessed."""
        return self._access_count
    
    def __str__(self):
        """String representation through proxy."""
        return f"[PROXY] {self._product}"
    
    def __repr__(self):
        """Representation through proxy."""
        return f"ProductProxy({repr(self._product)}, access_level='{self._access_level}')"
    
    # Allow proxy to be used in price calculations
    def __getattr__(self, name):
        """Delegate any other attribute access to the underlying product."""
        return getattr(self._product, name)

