import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
os.chdir("/Users/jijinsebastian/Workspace/Practice")
os.getcwd()

df = spark.read.parquet("sample_parquet")
df.printSchema()


df = df.withColumn("JoiningDate_AsString", df.EventTitle.cast("string"))
df.show()

df.repartition(3).write.csv("converted_csv.csv", mode="overwrite", header=True)