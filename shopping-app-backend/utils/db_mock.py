import json
import os

USERS_FILE = "users_data.json"
ADMINS_FILE = "admins_data.json"
PRODUCTS_FILE = "products_data.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def load_admins():
    if os.path.exists(ADMINS_FILE):
        with open(ADMINS_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_admins(admins):
    with open(ADMINS_FILE, 'w') as file:
        json.dump(admins, file, indent=4)

def load_products():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'r') as file:
            return json.load(file)
    else:
        return []

def save_products(products):
    with open(PRODUCTS_FILE, 'w') as file:
        json.dump(products, file, indent=4)

users_db = load_users()
admins_db = load_admins()
products_db = load_products()
