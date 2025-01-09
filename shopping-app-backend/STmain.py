import streamlit as st
import pandas as pd
from admin import Admin
from cart import Cart
from catalog import Catalog
from login import User
from payment import Payment
from utils.db_mock import users_db, save_users

catalog = Catalog()

def admin_page():
    st.title("Admin Page")

    admin_username = st.text_input("Admin Username")
    admin_password = st.text_input("Admin Password", type="password")
    
    if st.button("Login"):
        admin = Admin(admin_username, admin_password, catalog)
        
        if admin.login():
            st.success("Login successful!")
            action = st.selectbox("Choose action", ["Add Product", "Remove Product", "View Catalog", "View Users", "Remove User"])
            
            if action == "Add Product":
                add_product(admin)
            elif action == "Remove Product":
                remove_product(admin)
            elif action == "View Catalog":
                view_catalog(admin)
            elif action == "View Users":
                view_users()
            elif action == "Remove User":
                remove_user()

def add_product(admin):
    st.header("Add Product")
    product_name = st.text_input("Product Name")
    product_category = st.text_input("Product Category")
    product_price = st.number_input("Product Price", min_value=0.0)
    
    if st.button("Add Product"):
        if product_name and product_category and product_price > 0:
            new_product = {
                "id": len(catalog.products) + 1,
                "name": product_name,
                "category": product_category,
                "price": product_price
            }
            admin.add_product(new_product)
            st.success(f"Product '{product_name}' added successfully.")
        else:
            st.error("Please fill in all fields correctly.")

def remove_product(admin):
    st.header("Remove Product")
    product_id = st.number_input("Product ID to Remove", min_value=1)
    
    if st.button("Remove Product"):
        admin.remove_product(product_id)
        st.success(f"Product with ID {product_id} removed successfully.")

def view_catalog(admin):
    st.header("Catalog")
    st.dataframe(catalog.view_products())

def view_users():
    st.header("Registered Users")
    if users_db:
        users_df = pd.DataFrame(users_db.items(), columns=["Username", "Password"])
        st.dataframe(users_df)
    else:
        st.warning("No users found.")

def remove_user():
    st.header("Remove User")
    username_to_remove = st.text_input("Enter Username to Remove")
    
    if st.button("Remove User"):
        if username_to_remove in users_db:
            del users_db[username_to_remove]
            save_users(users_db)
            st.success(f"User '{username_to_remove}' has been removed.")
        else:
            st.error("User not found.")

def user_page():
    st.title("User Page")

    user_username = st.text_input("Username")
    
    if st.button("Login"):
        if user_username in users_db:
            user_password = st.text_input("Password", type="password")
            user = User(user_username, user_password)
            
            if user.login():
                st.success(f"Welcome {user_username}!")
                view_catalog_user(user)
        else:
            st.error("User not found. Do you want to register?")
            if st.button("Register"):
                register_user(user_username)

def view_catalog_user(user):
    st.header("Catalog")
    product_list = catalog.view_products().to_dict(orient="records")
    for product in product_list:
        st.write(f"{product['name']} - Rs. {product['price']} - {product['category']}")
    
    product_id_to_add = st.number_input("Enter Product ID to Add to Cart", min_value=1)
    quantity_to_add = st.number_input("Enter Quantity", min_value=1)
    
    if st.button("Add to Cart"):
        product_to_add = next((prod for prod in product_list if prod["id"] == product_id_to_add), None)
        if product_to_add:
            cart = Cart()
            cart.add_to_cart(product_to_add, quantity_to_add)
            st.success(f"{product_to_add['name']} added to cart.")
        else:
            st.error("Product not found in catalog.")
    
    checkout(cart)

def checkout(cart):
    if st.button("Checkout"):
        st.write("\nYour Cart:")
        total_amount = sum(item["product"]["price"] * item["quantity"] for item in cart.view_cart())
        for item in cart.view_cart():
            st.write(f"{item['product']['name']} x{item['quantity']} - Rs. {item['product']['price'] * item['quantity']}")
        st.write(f"\nTotal amount to be paid: Rs. {total_amount}")
        
        payment_method = st.selectbox("Choose Payment Method", ["UPI", "Debit Card"])
        payment = Payment(total_amount)
        payment.process_payment(payment_method)
        st.success("Thank you for your purchase!")

def register_user(username):
    new_password = st.text_input("Enter New Password", type="password")
    if new_password:
        users_db[username] = new_password
        save_users(users_db)
        st.success(f"User '{username}' registered successfully!")

def main():
    st.title("Demo Marketplace")
    
    user_type = st.selectbox("Are you an Admin or User?", ["Admin", "User"])
    
    if user_type == "Admin":
        admin_page()
    else:
        user_page()

if __name__ == "__main__":
    main()
