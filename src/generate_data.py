from faker import Faker
import pandas as pd
import random
import numpy as np

fake = Faker("fr_FR")

NB_CUSTOMERS = 10000
NB_PRODUCTS = 1000
NB_ORDERS = 100000

# ----------------------
# CUSTOMERS
# ----------------------

customers = []

for i in range(1, NB_CUSTOMERS + 1):
    customers.append({
        "customer_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "city": fake.city(),
        "country": "France",
        "signup_date": fake.date_between("-3y", "today")
    })

customers_df = pd.DataFrame(customers)

# ----------------------
# PRODUCTS
# ----------------------

categories = ["Electronics", "Home", "Books", "Sports", "Clothing"]

products = []

for i in range(1, NB_PRODUCTS + 1):
    products.append({
        "product_id": i,
        "product_name": fake.word().capitalize(),
        "category": random.choice(categories),
        "price": round(random.uniform(5, 500), 2)
    })

products_df = pd.DataFrame(products)

# ----------------------
# ORDERS
# ----------------------

orders = []

for i in range(1, NB_ORDERS + 1):

    customer_id = random.randint(1, NB_CUSTOMERS)
    product_id = random.randint(1, NB_PRODUCTS)
    quantity = random.randint(1, 5)

    order_date = fake.date_between("-2y", "today")

    # 5% de données bruitées (important pour ETL)
    if random.random() < 0.05:
        product_id = None

    orders.append({
        "order_id": i,
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "order_date": order_date
    })

orders_df = pd.DataFrame(orders)

# ----------------------
# PAYMENTS
# ----------------------

payments = []

payment_methods = ["Credit Card", "Paypal", "Bank Transfer"]

for i in range(1, NB_ORDERS + 1):

    amount = None
    if orders[i - 1]["product_id"] is not None:
        price = products_df.loc[products_df["product_id"] == orders[i - 1]["product_id"], "price"]
        if len(price) > 0:
            amount = float(price.iloc[0]) * orders[i - 1]["quantity"]

    payments.append({
        "payment_id": i,
        "order_id": i,
        "payment_method": random.choice(payment_methods),
        "amount": amount,
        "payment_date": fake.date_between("-2y", "today")
    })

payments_df = pd.DataFrame(payments)

# ----------------------
# EXPORT
# ----------------------

import os
os.makedirs("data", exist_ok=True)

customers_df.to_csv("data/customers.csv", index=False)
products_df.to_csv("data/products.csv", index=False)
orders_df.to_csv("data/orders.csv", index=False)
payments_df.to_csv("data/payments.csv", index=False)

print("CSV generated successfully")