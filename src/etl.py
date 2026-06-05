from pyspark.sql import SparkSession
from pyspark.sql.functions import col


spark = SparkSession.builder \
    .appName("ETL Project") \
    .getOrCreate()

print("Spark ready")

customers = spark.read.csv("data/customers.csv", header=True, inferSchema=True)
products = spark.read.csv("data/products.csv", header=True, inferSchema=True)
orders = spark.read.csv("data/orders.csv", header=True, inferSchema=True)
payments = spark.read.csv("data/payments.csv", header=True, inferSchema=True)

customers.show(5)
print('-----')
products.show(5)
print('-----')
orders.show(5)
print('-----')
payments.show(5)


orders = orders.dropna(subset=["customer_id", "product_id"])
products = products.dropna(subset=["product_id"])

sales = orders \
    .join(customers, "customer_id", "left") \
    .join(products, "product_id", "left") \
    .join(payments, "order_id", "left")

sales.show(5)


sales = sales.withColumn(
    "total_amount",
    col("quantity") * col("price")
)


sales.write.mode("overwrite").parquet("output/sales")

spark.stop()