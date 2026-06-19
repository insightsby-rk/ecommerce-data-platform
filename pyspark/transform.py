from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EcommerceTransform") \
    .getOrCreate()

customers = spark.read.csv(
    "data/raw/customers.csv",
    header=True,
    inferSchema=True
)

orders = spark.read.csv(
    "data/raw/orders.csv",
    header=True,
    inferSchema=True
)

joined_df = customers.join(
    orders,
    on="customer_id",
    how="inner"
)

print("Joined Data")
joined_df.show()

joined_df.write \
    .mode("overwrite") \
    .parquet("data/bronze/customer_orders")

print("Silver Layer Created")

spark.stop()
