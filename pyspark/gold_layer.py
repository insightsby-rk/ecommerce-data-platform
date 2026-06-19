from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum, avg

spark = SparkSession.builder \
    .appName("GoldLayer") \
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

gold_df = joined_df.groupBy(
    "customer_id",
    "name"
).agg(
    count("order_id").alias("total_orders"),
    sum("amount").alias("total_amount"),
    avg("amount").alias("avg_order_value")
)

print("Gold Layer")

gold_df.show()

spark.stop()