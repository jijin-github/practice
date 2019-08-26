from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]
df = sparkSession.createDataFrame(data)

print df,"jjjjjj",dir(df)
# df.write.csv("hdfs://cluster/user/hdfs/test/example.csv")
df.write.csv("dfs://Users/jijinsebastian/Workspace/Practice/example.csv")