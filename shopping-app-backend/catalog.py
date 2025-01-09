import pandas as pd
from utils.db_mock import load_products, save_products

class Catalog:
    def __init__(self):
        # Load products from JSON file
        self.products = load_products()  # Correctly load products using load_products
        self.categories = list({product["category"] for product in self.products})

    def add_product(self, product):
        """Add a product to the catalog and save changes."""
        self.products.append(product)
        save_products(self.products)  # Save the updated products list to JSON
        print("Product added successfully and saved.")

    def remove_product(self, product_id):
        """Remove a product by ID and save changes."""
        self.products = [product for product in self.products if product["id"] != product_id]
        save_products(self.products)  # Save the updated products list to JSON
        print("Product removed successfully and saved.")

    def add_category(self, category_name):
        """Add a new category."""
        if category_name not in self.categories:
            self.categories.append(category_name)
            print(f"Category '{category_name}' added.")

    def remove_category(self, category_name):
        """Remove an existing category."""
        self.categories = [cat for cat in self.categories if cat != category_name]
        print(f"Category '{category_name}' removed.")

    def view_products(self):
        """Return a DataFrame of products for display."""
        return pd.DataFrame(self.products)
