from src.ingestion.load import (
    create_spark,
    load_customers,
    load_products,
    load_orders,
    load_payments
)


from src.transformations.transform import build_sales

def run_pipeline():

    spark = create_spark()

    
    customers = load_customers(spark)
    products = load_products(spark)
    orders = load_orders(spark)
    payments = load_payments(spark)

    sales = build_sales(customers, products, orders, payments)

    sales.write.mode("overwrite").parquet("output/gold/sales")

    print("Pipeline finished successfully")

    spark.stop()


if __name__ == "__main__":
    run_pipeline()