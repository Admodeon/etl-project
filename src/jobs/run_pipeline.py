from src.ingestion.bronze import create_spark, load_bronze
from src.transformations.silver import build_silver
from src.transformations.gold import build_gold

def run_pipeline():

    # 1. Spark session
    spark = create_spark()

    # 2. BRONZE
    customers, products, orders, payments = load_bronze(spark)

    # 3. SILVER
    customers_s, products_s, orders_s, payments_s = build_silver(
        customers, products, orders, payments
    )

    # 4. GOLD
    sales = build_gold(
        customers_s, products_s, orders_s, payments_s
    )

    # 5. OUTPUT
    sales.write.mode("overwrite").parquet("output/gold/sales")

    print("Pipeline finished successfully")

    spark.stop()


if __name__ == "__main__":
    run_pipeline()