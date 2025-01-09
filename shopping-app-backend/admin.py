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
        try:
            product_price = float(input("Enter product price: "))
            new_product = {
                "id": len(self.catalog.products) + 1,
                "name": product_name,
                "category": product_category,
                "price": product_price
            }
            self.catalog.add_product(new_product)
            print(f"\nProduct added successfully:\n{pd.DataFrame([new_product])}")
            print(f"\nUpdated Catalog:\n{pd.DataFrame(self.catalog.products)}")
            
        except ValueError:
            print("Invalid input. Please enter a numeric value for price.")

    def remove_product(self):
        """Handles removing a product from the catalog."""
        try:
            product_id_to_remove = int(input("Enter product ID to remove: "))
            product_found = any(p["id"] == product_id_to_remove for p in self.catalog.products)
            if not product_found:
                print(f"Product with ID {product_id_to_remove} not found.")
                return

            self.catalog.products = self.catalog.remove_product(product_id_to_remove)
            print(f"Product with ID {product_id_to_remove} removed successfully.")
            print(f"\nUpdated Catalog:\n{pd.DataFrame(self.catalog.products)}")
        except ValueError:
            print("Invalid input. Please enter a numeric value for product ID.")

    def view_catalog(self):
        """Displays the current catalog."""
        if not self.catalog.products:
            print("The catalog is currently empty.")
        else:
            print("\nCurrent Product Catalog:")
            print(pd.DataFrame(self.catalog.products))

