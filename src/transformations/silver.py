def build_silver(customers, products, orders, payments):

    # CLEAN ORDERS
    orders_clean = orders.dropna(subset=["customer_id", "product_id"])

    # CLEAN PRODUCTS
    products_clean = products.dropna(subset=["product_id"])

    # CLEAN CUSTOMERS
    customers_clean = customers.dropna(subset=["customer_id"])

    # CLEAN PAYMENTS 
    payments_clean = payments.dropna(subset=["order_id"])

    return customers_clean, products_clean, orders_clean, payments_clean