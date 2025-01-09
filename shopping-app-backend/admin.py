import pandas as pd
from catalog import Catalog

class Admin:
    def __init__(self, username, password, catalog):
        self.username = username
        self.password = password
        self.admin_users = {"admin": "admin123"} 
        self.catalog = catalog

    def login(self):
        """Checks if the entered credentials are valid."""
        if self.username in self.admin_users and self.admin_users[self.username] == self.password:
            return True
        return False

    def add_product(self):
        """Handles adding a product to the catalog."""
        product_name = input("Enter product name: ")
        product_category = input("Enter product category: ")
        product_price = float(input("Enter product price: "))
        new_product = {
            "id": len(self.catalog.products) + 1,
            "name": product_name,
            "category": product_category,
            "price": product_price
        }
        self.catalog.add_product(new_product)
        print(f"Product added: \n{pd.DataFrame([new_product])}")
        print("\nUpdated catalog: \n", pd.DataFrame(self.catalog.products))

    def remove_product(self):
        """Handles removing a product from the catalog."""
        product_id_to_remove = int(input("Enter product ID to remove: "))
        self.catalog.products = self.catalog.remove_product(product_id_to_remove)
        print(f"Product with ID {product_id_to_remove} removed.")
        print("\nUpdated catalog after removal: \n", pd.DataFrame(self.catalog.products))

    def add_category(self):
        """Handles adding a category."""
        category_name = input("Enter new category name: ")
        self.catalog.add_category(category_name)
        print(f"Updated categories: {self.catalog.categories}")

    def remove_category(self):
        """Handles removing a category."""
        category_name = input("Enter category name to remove: ")
        self.catalog.remove_category(category_name)
        print(f"Updated categories: {self.catalog.categories}")

    def view_catalog(self):
        """Displays the current catalog."""
        print("\nCurrent Catalog:")
        print(pd.DataFrame(self.catalog.products))
