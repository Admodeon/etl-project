from src.ingestion.bronze import create_spark, load_bronze
from src.transformations.silver import build_silver
from src.transformations.gold import build_gold
from src.ingestion.api import load_users_api

def run_pipeline():

    # 1. Spark session
    spark = create_spark()

    # 2. BRONZE
    customers, products, orders, payments = load_bronze(spark)
    users = load_users_api(spark)

    # 3. SILVER
    customers_s, products_s, orders_s, payments_s, users_s = build_silver(
    customers, products, orders, payments, users
)

    print("CUSTOMERS")
    customers_s.printSchema()
    customers_s.show(5)

    print("PRODUCTS")
    products_s.printSchema()
    products_s.show(5)

    print("ORDERS")
    orders_s.printSchema()
    orders_s.show(5)

    print("PAYMENTS")
    payments_s.printSchema()
    payments_s.show(5)

    if users_s:
        print("USERS")
        users_s.printSchema()
        users_s.show(5)

    # 4. GOLD
    sales = build_gold(
        customers_s, products_s, orders_s, payments_s, users_s
    )

    print("GOLD - SALES SCHEMA")
    sales.printSchema()

    print("GOLD - SALES SAMPLE")
    sales.show(20, truncate=False)


    # 5. OUTPUT

    sales.write.mode("overwrite").parquet("output/gold/sales")

    print("Pipeline finished successfully")

    spark.stop()


if __name__ == "__main__":
    run_pipeline()