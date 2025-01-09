from admin import Admin
from cart import Cart
from catalog import Catalog
from login import User
from payment import Payment
from utils.db_mock import users_db, save_users 


def admin_page(catalog):
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    admin = Admin(admin_username, admin_password, catalog)

    if admin.login():
        print("Admin login successful!")
        while True:
            print("\nAdmin actions:")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Add Category")
            print("4. Remove Category")
            print("5. View Catalog")
            print("6. Exit")

            choice = int(input("Choose an action (1-6): "))
            if choice == 1:
                admin.add_product()
            elif choice == 2:
                admin.remove_product()
            elif choice == 3:
                admin.add_category()
            elif choice == 4:
                admin.remove_category()
            elif choice == 5:
                admin.view_catalog()
            elif choice == 6:
                print("Exiting admin page...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid admin credentials.")


def user_login():
    print("\nUser Login:")
    user_username = input("Enter username: ")
    
    if user_username in users_db:
        user_password = input("Enter password: ")
        user = User(user_username, user_password)
        
        if user.login():
            print("User login successful!")
            catalog = Catalog()

            print("\nCatalog:")
            product_list = catalog.view_products().to_dict(orient='records')
            for product in product_list:
                print(f"{product['name']} - Rs. {product['price']} - {product['category']}")

            print("\nUser adds products to cart:")
            product_id_to_add = int(input("Enter product ID to add to cart: "))
            quantity_to_add = int(input("Enter quantity to add: "))

            product_to_add = next((prod for prod in product_list if prod['id'] == product_id_to_add), None)
            if product_to_add:
                cart = Cart()
                cart.add_to_cart(product_to_add, quantity_to_add)
                print(f"{product_to_add['name']} added to cart.")
            else:
                print("Product not found in catalog.")
            
            print("\nYour Cart:")
            for item in cart.view_cart():
                print(f"{item['product']['name']} x{item['quantity']} - Rs. {item['product']['price'] * item['quantity']}")
            
            total_amount = sum(item['product']['price'] * item['quantity'] for item in cart.view_cart())
            print(f"\nTotal amount to be paid: Rs. {total_amount}")
            
            payment_method = input("Choose payment method (UPI/Debit Card): ")
            payment = Payment(total_amount)
            payment.process_payment(payment_method)
            print("Thank you for your purchase!")
        else:
            print("Invalid password. Please try again.")
    else:
        print("User not found. Do you want to register? (yes/no)")
        choice = input().lower()
        if choice == 'yes':
            new_password = input("Enter a new password: ")
            users_db[user_username] = new_password
            save_users(users_db) 
            print(f"Registration successful! {user_username} is now registered.")
            user_login()  
        else:
            print("Exiting...")

def main():
    print("Welcome to the Demo Marketplace!")

    user_type = input("Are you an Admin or User? (Enter 'Admin' or 'User'): ").lower()

    if user_type == 'admin':
        catalog = Catalog()
        admin_page(catalog)
    elif user_type == 'user':
        user_login()  
    else:
        print("Invalid input. Please enter 'admin' or 'user'.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
