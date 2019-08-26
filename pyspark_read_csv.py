import os
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, when, unix_timestamp
from pyspark.sql.types import DateType, DoubleType, IntegerType, StringType, StructField, StructType


spark = SparkSession.builder.getOrCreate()
os.chdir("/Users/jijinsebastian/Workspace/Practice")
os.getcwd()

df1 = spark.read.csv("sample.csv", header=True)
df1.printSchema()
df1.show()

schema = StructType([
    StructField("Start Date", StringType(), True),
    StructField("Start Time", StringType(), True),
    StructField("End Date", StringType(), True),
    StructField("End Time", StringType(), True),
    StructField("Event Title", StringType(), True)
])



df1 = spark.read.csv("sample.csv", header=True, schema=schema)
df1.printSchema()
df1.show()

df1 = df1.withColumnRenamed("Start Date", "StartDate")
df1 = df1.withColumnRenamed("Start Time", "StartTime")
df1 = df1.withColumnRenamed("End Date", "EndDate")
df1 = df1.withColumnRenamed("End Time", "EndTime")
df1 = df1.withColumnRenamed("Event Title", "EventTitle")


df1.where(df1['StartDate'] == df1['EndDate']).withColumn("Status", when(df1["EventTitle"] == "Social Studies Dept", "Not CUrr").otherwise("Curriculam..")).show()


# Write to parquet file

# df1.repartition("EventTitle").write.parquet("sample_parquet", "overwrite")