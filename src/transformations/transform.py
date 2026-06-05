from pyspark.sql.functions import col

def clean_orders(orders):
    return orders.dropna(subset=["customer_id", "product_id"])


def build_sales(customers, products, orders, payments):

    # 1. clean
    orders_clean = clean_orders(orders)

    # 2. join
    sales = orders_clean \
        .join(customers, "customer_id", "left") \
        .join(products, "product_id", "left") \
        .join(payments, "order_id", "left")

    # 3. enrichissement
    sales = sales.withColumn(
        "total_amount",
        col("quantity") * col("price")
    )

    return sales