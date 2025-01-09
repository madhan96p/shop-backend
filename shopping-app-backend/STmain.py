import streamlit as st
from admin import Admin
from cart import Cart
from catalog import Catalog
from login import User
from payment import Payment
from utils.db_mock import users_db, save_users
import pandas as pd

def admin_page(catalog):
    admin_username = st.text_input("Enter admin username: ")
    admin_password = st.text_input("Enter admin password: ", type='password')
    if st.button("Login as Admin"):
        admin = Admin(admin_username, admin_password, catalog)
        if admin.login():
            st.success("Admin login successful!")
            action = st.selectbox("Admin actions", ["", "Add Product", "Remove Product", "Add Category", "Remove Category", "View Catalog"])

            # Handling each admin action
            if action == "Add Product":
                product_name = st.text_input("Enter product name:")
                product_category = st.text_input("Enter product category:")
                product_price = st.number_input("Enter product price:", min_value=0)
                if st.button("Add Product"):
                    if product_name and product_category and product_price:
                        new_product = {"id": len(catalog.view_products()) + 1, "name": product_name, "category": product_category, "price": product_price}
                        catalog.add_product(new_product)
                        st.success(f"Product '{product_name}' added successfully!")
                    else:
                        st.error("Please fill in all the fields.")

            elif action == "Remove Product":
                product_list = catalog.view_products()
                product_to_remove = st.selectbox("Select product to remove", product_list['name'])
                if st.button("Remove Product"):
                    product_to_remove_id = product_list[product_list['name'] == product_to_remove]['id'].values[0]
                    catalog.remove_product(product_to_remove_id)
                    st.success(f"Product '{product_to_remove}' removed successfully!")

            elif action == "Add Category":
                new_category = st.text_input("Enter new category:")
                if st.button("Add Category"):
                    # Add category logic (Assuming you have a method for that)
                    st.success(f"Category '{new_category}' added successfully!")

            elif action == "Remove Category":
                # Remove category logic (Provide the list of categories to remove)
                st.warning("Removing category feature is not implemented yet.")

            elif action == "View Catalog":
                st.write("Product Catalog:")
                st.dataframe(catalog.view_products())

        else:
            st.error("Invalid admin credentials.")

# Function for User Login
def user_login():
    user_username = st.text_input("Enter username: ")
    
    if user_username in users_db:
        user_password = st.text_input("Enter password: ", type='password')
        if st.button("Login"):
            user = User(user_username, user_password)
            if user.login():
                st.success("User login successful!")
                
                # Catalog view
                catalog = Catalog()
                st.write("Catalog:")
                product_list = catalog.view_products()
                st.dataframe(product_list[['name', 'price', 'category']])

                # Add to cart
                st.write("User adds products to cart:")
                product_id_to_add = st.number_input("Enter product ID to add to cart:", min_value=1, max_value=len(product_list), step=1)
                quantity_to_add = st.number_input("Enter quantity to add:", min_value=1, step=1)

                if st.button("Add to Cart"):
                    product_to_add = product_list[product_list['id'] == product_id_to_add]
                    if not product_to_add.empty:
                        cart = Cart()
                        cart.add_to_cart(product_to_add.iloc[0].to_dict(), quantity_to_add)
                        st.success(f"{product_to_add['name'].values[0]} added to cart.")
                    else:
                        st.error("Product not found in catalog.")

                # Display Cart
                st.write("Your Cart:")
                cart_items = Cart().view_cart()
                if cart_items:
                    cart_df = pd.DataFrame([{
                        'Product Name': item['product']['name'],
                        'Quantity': item['quantity'],
                        'Total Price': item['product']['price'] * item['quantity']
                    } for item in cart_items])
                    st.dataframe(cart_df)
                    
                    # Payment
                    total_amount = sum(item['product']['price'] * item['quantity'] for item in cart_items)
                    st.write(f"Total amount to be paid: Rs. {total_amount}")

                    payment_method = st.selectbox("Choose payment method", ["UPI", "Debit Card"])
                    if st.button("Pay Now"):
                        payment = Payment(total_amount)
                        payment.process_payment(payment_method)
                        st.success("Thank you for your purchase!")
            else:
                st.error("Invalid password. Please try again.")
        else:
            st.error("User not found. Do you want to register?")
            if st.button("Register"):
                new_password = st.text_input("Enter a new password: ", type="password")
                if new_password:
                    users_db[user_username] = new_password
                    save_users(users_db)  # Save the new user to the file
                    st.success(f"Registration successful! {user_username} is now registered.")
                    user_login()  # Automatically log the user in
    else:
        st.write("No such user found.")

def main():
    st.title("Welcome to the Demo Marketplace!")

    user_type = st.selectbox("Are you an Admin or User?", ["", "Admin", "User"])

    if user_type == "Admin":
        catalog = Catalog()
        admin_page(catalog)
    elif user_type == "User":
        user_login()
    else:
        st.error("Please choose either Admin or User.")

if __name__ == "__main__":
    main()
