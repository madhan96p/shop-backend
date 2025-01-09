class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        self.cart_items.append({"product": product, "quantity": quantity})

    def remove_from_cart(self, product_id):
        self.cart_items = [item for item in self.cart_items if item["product"]["id"] != product_id]

    def view_cart(self):
        return self.cart_items
