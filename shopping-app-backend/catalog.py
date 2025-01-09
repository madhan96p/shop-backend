class Catalog:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Boots", "category": "Footwear", "price": 1000},
            {"id": 2, "name": "Coat", "category": "Clothing", "price": 1500},
        ]
    
    def view_products(self):
        return self.products
    
    def add_product(self, product):
        self.products.append(product)

    def update_product(self, product_id, updated_product):
        for product in self.products:
            if product["id"] == product_id:
                product.update(updated_product)
                break
