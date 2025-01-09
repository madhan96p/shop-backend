import pandas as pd
from utils.db_mock import products_db

class Catalog:
    def __init__(self):
        self.products = products_db 
        
    def view_products(self):
        """Returns product list as a pandas DataFrame."""
        return pd.DataFrame(self.products)
    
    def add_product(self, product):
        """Adds a new product to the catalog."""
        self.products.append(product)
    
    def update_product(self, product_id, updated_product):
        """Updates product details based on product_id."""
        for product in self.products:
            if product["id"] == product_id:
                product.update(updated_product)
                break
