from pyspark.sql import SparkSession

def create_spark():
    return SparkSession.builder.appName("ETL").getOrCreate()


def load_bronze(spark):
    customers = spark.read.csv("data/customers.csv", header=True, inferSchema=True)
    products = spark.read.csv("data/products.csv", header=True, inferSchema=True)
    orders = spark.read.csv("data/orders.csv", header=True, inferSchema=True)
    payments = spark.read.csv("data/payments.csv", header=True, inferSchema=True)

    return customers, products, orders, payments