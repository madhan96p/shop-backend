# Shopping App Backend 🛍️

This is the backend for a simple shopping app! It handles user login, admin login, product catalog, shopping cart, and simulates payments. 😊

## Project Files 🗂️

- **[`admin.py`](https://github.com/madhan96p/shop-backend/blob/main/shopping-app-backend/admin.py)**: Admin login and management.
- **[`cart.py`](https://github.com/madhan96p/shop-backend/blob/main/shopping-app-backend/cart.py)**: Manage shopping cart (add, remove, view items).
- **[`catalog.py`](https://github.com/madhan96p/shop-backend/blob/main/shopping-app-backend/catalog.py)**: Manage product catalog (view and add products).
- **[`login.py`](https://github.com/madhan96p/shop-backend/blob/main/shopping-app-backend/login.py)**: User and admin login validation.
- **[`main.py`](https://github.com/madhan96p/shop-backend/blob/main/shopping-app-backend/main.py)**: The main app that ties everything together.
- **[`payment.py`](https://github.com/madhan96p/shop-backend/blob/main/shopping-app-backend/payment.py)**: Simulates the payment process.
- **[`utils/db_mock.py`](https://github.com/madhan96p/shop-backend/blob/main/shopping-app-backend/utils/db_mock.py)**: Functions for loading and saving mock data (users, admins, products).

## Requirements ⚙️

- Python 3.x
- Libraries: `json`, `os`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Features 🎉

- **User Login**: Users can log in with their credentials.
- **Admin Login**: Admins can log in to manage the app.
- **Product Catalog**: Admins can manage the product catalog.
- **Shopping Cart**: Users can add/remove products and view their cart.
- **Payment Simulation**: A simple payment process is simulated.

## How to Start 🚀

1. Clone the repo:

   ```bash
   git clone https://github.com/madhan96p/shop-backend.git
   cd shopping-app-backend
   ```

2. Install dependencies.

3. Run the app:

   ```bash
   python main.py
   ```

   Now you can log in as a user or admin, manage products, and simulate payments! 💳

## Mock Data 📂

- **Users**: Stored in `users_data.json`.
- **Admins**: Stored in `admins_data.json`.
- **Products**: Stored in `products_data.json`.
