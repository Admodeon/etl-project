from pyspark.sql import SparkSession

def create_spark():
    return SparkSession.builder \
        .appName("ETL Project") \
        .getOrCreate()


def load_customers(spark):
    return spark.read.csv(
        "data/customers.csv",
        header=True,
        inferSchema=True
    )


def load_products(spark):
    return spark.read.csv(
        "data/products.csv",
        header=True,
        inferSchema=True
    )


def load_orders(spark):
    return spark.read.csv(
        "data/orders.csv",
        header=True,
        inferSchema=True
    )


def load_payments(spark):
    return spark.read.csv(
        "data/payments.csv",
        header=True,
        inferSchema=True
    )