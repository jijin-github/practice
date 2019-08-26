import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
os.chdir("/Users/jijinsebastian/Workspace/Practice")
os.getcwd()

df1 = spark.read.csv("product.csv", header=True)
df1.printSchema()
df1.show()

df2 = spark.read.csv("OrderDetails.csv", header=True)
df2.printSchema()
df2.show()

df3 = df1.join(df2, df1["ProductID"] == df2["ProductID"], "inner")
df3.show()

df3.createOrReplaceTempView("table1")
spark.sql(
    """
    SELECT COUNT(ProductName), AVG(Quantity), OrderID FROM table1 GROUP BY OrderID
    """).show()