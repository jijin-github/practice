from pyspark.sql import Row
from collections import OrderedDict


class data_frame_class(data_class):

    def get_data_frame(self):
        dta = self.data_list
        dtaRdd = spark.sparkContext.parallelize(dta).map(lambda x: Row(**OrderedDict(sorted(x.items()))))
        dtaDF = spark.createDataFrame(dtaRdd)
        return dta


print(data_frame_class().get_data_frame())from pyspark.sql import Row
from collections import OrderedDict

from pyspark.sql.types import DateType, DoubleType, IntegerType, StringType, StructField, StructType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("adds", StringType(), True),
    StructField("load_date", DateType(), True)
])

df1 = spark.read.csv("input.csv", header=True, schema=schema)
df1.printSchema()

df1.show()

# df1.write.csv("result/valid.csv", mode="overwrite", header=True)
# df1.write.csv("result/invalid.csv", mode="overwrite", header=True)


df1.createOrReplaceTempView("table1")
spark.sql(
    """
    SELECT COUNT(adds) AS addsCount, adds FROM table1 GROUP BY adds ORDER BY COUNT(adds) DESC LIMIT 1
    """).show()

def validate_dict(dict1, dict2):
    result = []
    for key, value in dict2.items():
        if value == "boolean":
            result.append(key)
    for key, value in dict1.items():
        if value == "string":
            result.append(key)
    return result

data_type1={
            "a":"string",
            "b":"int",
            "c":"string",
            "d":"boolean"
        }

data_type2={
    "a":"string",
    "b":"boolean",
    "c":"boolean",
    "d":"int"
}

# sample input = [57, 743, 1, 10, 57, 100, 57, 1000, 100, 1]
# expected output = [(57, 743), (57, 10), (57, 1000), (1, 1), (1, 100), (100, 1), (100, 100)]

print(validate_dict(data_type1, data_type2))

def get_tuple_list(input_list):
    result = []
    count_list = []
    for i in input_list:
        no_count = input_list.count(i)
        count_list.append(no_count)
    detail_dict = zip(input_list, count_list)
    dict_order = sorted(detail_dict, key=lambda x: x[1])
    for i in range(0, len(input_list)//2):
        result.append((dict_order[len(input_list)-i-1][0], dict_order[i][0]))
    return result

sample_input = [57, 743, 1, 10, 57, 100, 57, 1000, 100, 1]
print(get_tuple_list(sample_input))