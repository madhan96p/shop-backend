import streamlit as st
import pandas as pd
from admin import Admin
from cart import Cart
from catalog import Catalog
from login import User
from payment import Payment
from utils.db_mock import users_db, save_users

catalog = Catalog()

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "user_logged_in" not in st.session_state:
    st.session_state.user_logged_in = False

if "cart" not in st.session_state:
    st.session_state.cart = Cart()

def admin_page():
    st.title("Admin Dashboard")

    if not st.session_state.admin_logged_in:
        admin_username = st.text_input("Admin Username")
        admin_password = st.text_input("Admin Password", type="password")

        if st.button("Login"):
            admin = Admin(admin_username, admin_password, catalog)
            if admin.login():
                st.session_state.admin_logged_in = True
                st.session_state.admin = admin
                st.success("Login successful!")
            else:
                st.error("Invalid credentials")

    if st.session_state.admin_logged_in:
        action = st.selectbox("Choose action", ["Add Product", "Remove Product", "View Catalog", "View Users", "Remove User"])

        if action == "Add Product":
            add_product(st.session_state.admin)
        elif action == "Remove Product":
            remove_product(st.session_state.admin)
        elif action == "View Catalog":
            view_catalog()
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

def view_catalog():
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

# User Page
def user_page():
    st.title("User Dashboard")

    if not st.session_state.user_logged_in:
        user_username = st.text_input("Username")
        user_password = st.text_input("Password", type="password")

        if st.button("Login"):
            if user_username in users_db and users_db[user_username] == user_password:
                st.session_state.user_logged_in = True
                st.session_state.user = User(user_username, user_password)
                st.success(f"Welcome {user_username}!")
            else:
                st.error("Invalid credentials or user not found.")

    if st.session_state.user_logged_in:
        view_catalog_user()

def view_catalog_user():
    st.header("Available Products")
    product_list = catalog.view_products().to_dict(orient="records")

    for product in product_list:
        st.write(f"**{product['name']}** - Rs. {product['price']} - ({product['category']})")

    product_id_to_add = st.number_input("Enter Product ID to Add to Cart", min_value=1, step=1)
    quantity_to_add = st.number_input("Enter Quantity", min_value=1, step=1)

    if st.button("Add to Cart"):
        product_to_add = next((prod for prod in product_list if prod["id"] == product_id_to_add), None)
        if product_to_add:
            st.session_state.cart.add_to_cart(product_to_add, quantity_to_add)
            st.success(f"{product_to_add['name']} added to cart.")
        else:
            st.error("Product not found in catalog.")

    checkout()

def checkout():
    st.header("Your Cart")

    cart_items = st.session_state.cart.view_cart()
    if not cart_items:
        st.warning("Your cart is empty.")
        return

    total_amount = sum(item["product"]["price"] * item["quantity"] for item in cart_items)

    for item in cart_items:
        st.write(f"{item['product']['name']} x{item['quantity']} - Rs. {item['product']['price'] * item['quantity']}")

    st.write(f"**Total: Rs. {total_amount}**")

    payment_method = st.selectbox("Choose Payment Method", ["UPI", "Debit Card"])
    
    if st.button("Proceed to Payment"):
        payment = Payment(total_amount)
        payment.process_payment(payment_method)
        st.success("Payment Successful! Thank you for shopping.")

# Main function
def main():
    st.title("Demo Marketplace")

    user_type = st.radio("Are you an Admin or User?", ["Admin", "User"])

    if user_type == "Admin":
        admin_page()
    else:
        user_page()

if __name__ == "__main__":
    main()
