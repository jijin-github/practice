# # import pyspark class Row from module sql
# from pyspark.sql import *
# from pyspark import SparkContext
# #
# # Create Example Data - Departments and Employees
#
# # Create the Departments
# department1 = Row(id='123456', name='Computer Science')
# department2 = Row(id='789012', name='Mechanical Engineering')
# department3 = Row(id='345678', name='Theater and Drama')
# department4 = Row(id='901234', name='Indoor Recreation')
#
# # Create the Employees
# Employee = Row("firstName", "lastName", "email", "salary")
# employee1 = Employee('michael', 'armbrust', 'no-reply@berkeley.edu', 100000)
# employee2 = Employee('xiangrui', 'meng', 'no-reply@stanford.edu', 120000)
# employee3 = Employee('matei', None, 'no-reply@waterloo.edu', 140000)
# employee4 = Employee(None, 'wendell', 'no-reply@berkeley.edu', 160000)
#
# # Create the DepartmentWithEmployees instances from Departments and Employees
# departmentWithEmployees1 = Row(department=department1, employees=[employee1, employee2])
# departmentWithEmployees2 = Row(department=department2, employees=[employee3, employee4])
# departmentWithEmployees3 = Row(department=department3, employees=[employee1, employee4])
# departmentWithEmployees4 = Row(department=department4, employees=[employee2, employee3])
#
# print(department1)
# print(employee2)
# print(departmentWithEmployees1.employees[0].email)
#
# departmentsWithEmployeesSeq1 = [departmentWithEmployees1, departmentWithEmployees2]
#
# sc = SparkContext()
# sqlContext = SQLContext(sc)
# df1 = sqlContext.createDataFrame(departmentsWithEmployeesSeq1)
#
# print df1,'LLLL'
#
# display(df1)


# spark = SparkSession.builder.master("local").appName("Word Count").config("spark.some.config.option", "some-value") .getOrCreate()


# http://www.learnbymarketing.com/1100/pyspark-joins-by-example/
from pyspark.sql import *
from pyspark import SparkContext

sc = SparkContext()
sqlContext = SQLContext(sc)
spark = sqlContext

valuesA = [('Pirate', 1), ('Monkey', 2), ('Ninja', 3), ('Spaghetti', 4)]
TableA = spark.createDataFrame(valuesA, ['name', 'id'])

valuesB = [('Rutabaga', 1), ('Pirate', 2), ('Ninja', 3), ('Darth Vader', 4)]
TableB = spark.createDataFrame(valuesB, ['name', 'id'])

TableA.show()
TableB.show()

columns_to_drop = ['id']
TableB = TableB.drop(*columns_to_drop)
TableB.show()

# ta = TableA.alias('ta')
# tb = TableB.alias('tb')
#
# # Inner join
# inner_join = ta.join(tb, ta.name == tb.name)
# inner_join.show()
#
# # Left Join
# left_join = ta.join(tb, ta.name == tb.name, how='left') # Could also use 'left_outer'
# left_join.show()
#
# right_join = ta.join(tb, ta.name == tb.name,how='right') # Could also use 'right_outer'
# right_join.show()


# sc.textFile("/Users/jijinsebastian/Downloads/C2ImportCalEventSample.csv") \
#     .map(lambda line: line.split(",")) \
#     .filter(lambda line: len(line)<=1) \
#     .collect()