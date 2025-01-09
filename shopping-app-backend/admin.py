class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin_users = {"admin": "admin123"}  
    
    def login(self):
        if self.username in self.admin_users and self.admin_users[self.username] == self.password:
            return True
        else:
            return False

    def add_product(self, catalog, product):
        catalog.append(product)
    
    def remove_product(self, catalog, product_id):
        catalog = [product for product in catalog if product["id"] != product_id]
        return catalog
    
    def add_category(self, categories, category_name):
        categories.append(category_name)
    
    def remove_category(self, categories, category_name):
        categories.remove(category_name)
