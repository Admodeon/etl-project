from pyspark.sql.functions import col

def build_gold(customers, products, orders, payments):

    sales = orders \
        .join(customers, "customer_id", "left") \
        .join(products, "product_id", "left") \
        .join(payments, "order_id", "left")

    sales = sales.withColumn(
        "total_amount",
        col("quantity") * col("price")
    )

    sales = sales.withColumn(
        "is_high_value",
        col("total_amount") > 200
    )

    return sales