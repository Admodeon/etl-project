from pyspark.sql.functions import col

def build_silver(customers, products, orders, payments, users=None):

    orders_clean = orders.dropna(subset=["customer_id", "product_id"])
    products_clean = products.dropna(subset=["product_id"])
    customers_clean = customers.dropna(subset=["customer_id"])
    payments_clean = payments.dropna(subset=["order_id"])

    users_clean = None
    if users is not None:
        users_clean = users.select(
            col("user_id").alias("customer_id"),
            col("name").alias("api_name"),
            col("email").alias("api_email"),
            col("city").alias("api_city"),
            col("company_name").alias("api_company")
        )

    return customers_clean, products_clean, orders_clean, payments_clean, users_clean