from admin import Admin
from cart import Cart
from catalog import Catalog
from login import User
from payment import Payment

admin_user = Admin("admin", "admin123")
normal_user = User("user1", "password1")

cart = Cart()
catalog = Catalog()

def main():
    print("Welcome to the Demo Marketplace!")
    
    user_type = input("Are you an Admin or User? (Enter 'Admin' or 'User'): ").lower()
    
    if user_type == 'admin':
        print("\nAdmin Login:")
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")
        admin = Admin(admin_username, admin_password)
        
        if admin.login():
            print("Admin login successful!")
            print("\nAdmin actions:")
            
            new_product = {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 20000}
            admin.add_product(catalog.products, new_product)
            print("Product added: ", new_product)
            print("Updated catalog: ", catalog.view_products())
            
            admin.add_category(catalog.products, "Home Appliances")
            print("Updated categories: ", ["Footwear", "Clothing", "Electronics", "Home Appliances"])
        
        else:
            print("Invalid admin credentials.")
    
    elif user_type == 'user':
        print("\nUser Login:")
        user_username = input("Enter username: ")
        user_password = input("Enter password: ")
        user = User(user_username, user_password)
        
        if user.login():
            print("User login successful!")
            
            print("\nCatalog:")
            for product in catalog.view_products():
                print(f"{product['name']} - Rs. {product['price']} - {product['category']}")
            
            print("\nUser adds products to cart:")
            product_id_to_add = int(input("Enter product ID to add to cart: "))
            quantity_to_add = int(input("Enter quantity to add: "))
            
            product_to_add = next((prod for prod in catalog.view_products() if prod['id'] == product_id_to_add), None)
            if product_to_add:
                cart.add_to_cart(product_to_add, quantity_to_add)
                print(f"{product_to_add['name']} added to cart.")
            else:
                print("Product not found in catalog.")
            
            print("\nYour Cart:")
            for item in cart.view_cart():
                print(f"{item['product']['name']} x{item['quantity']} - Rs. {item['product']['price'] * item['quantity']}")
            
            try:
                product_id_to_remove = int(input("Enter product ID to remove from cart: "))
                cart.remove_from_cart(product_id_to_remove)
                print("Item removed from cart.")
            except ValueError as e:
                print('User not removed anything', e)

            total_amount = sum(item['product']['price'] * item['quantity'] for item in cart.view_cart())
            print(f"\nTotal amount to be paid: Rs. {total_amount}")
            
            payment_method = input("Choose payment method (UPI/Debit Card): ")
            payment = Payment(total_amount)
            payment.process_payment(payment_method)
            print("Thank you for your purchase!")
        
        else:
            print("Invalid user credentials.")
    
    else:
        print("Invalid input. Please enter 'admin' or 'user'.")

if __name__ == "__main__":
    main()
