from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Parquet Join Example") \
    .getOrCreate()

try:
    # Path to the Parquet files
    parquet_file1 = 'FlowExecution.parquet'
    parquet_file2 = 'ApexTrigger.parquet'

    # Read the Parquet files into DataFrames and select required columns
    df1 = spark.read.parquet(parquet_file1).select("request_id", "CPU_TIME", "ENTRY_POINT")
    df2 = spark.read.parquet(parquet_file2).select("request_id", "CPU_TIME", "TRIGGER_NAME", "ENTITY_NAME")

    # Perform the join based on the 'request_id' column
    joined_df = df1.join(df2, on='request_id', how='inner')

   ## Filter the joined DataFrame for 'ENTITY_NAME' == <entityname>
    account_df = joined_df.filter(joined_df["ENTITY_NAME"] == "placeholder")

    # Group by 'ENTITY_NAME' and aggregate the CPU_TIME
    aggregate_df = account_df.groupBy("ENTITY_NAME").agg(F.sum("CPU_TIME").alias("Total_CPU_TIME"))

    # Show the aggregated DataFrame
    aggregate_df.show()


except Exception as e:
    print("An error occurred:", e)

finally:
    # Stop the SparkSession
    spark.stop()
