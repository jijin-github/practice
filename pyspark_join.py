df5 = spark.read.csv("employee.csv", header=True, inferSchema=True)
df5.printSchema()
df5.show()

df6 = spark.read.csv("department.csv", header=True, inferSchema=True)
df6.printSchema()
df6.show()

df7 = df5.join(df6, df5["ID"] == df6["EmployeeID"], "inner").drop("EmployeeID")
df7.printSchema()
df7.show()

df7.createOrReplaceTempView("table")
spark.sql(
    """
    SELECT count(Name) as TotalNumberOfEmployees, avg(Salary) as AverageSalary, DepartmentName
    FROM table
    GROUP BY DepartmentName
    """).show()

timeFmt = "yyyy-MM-dd'T'HH:mm:ss"
timeDiff = (unix_timestamp("OnboardedDate", format=timeFmt)
            - unix_timestamp("JoiningDate", format=timeFmt)) / (60*60*24)
df8 = df7.withColumn("IdleDuration", timeDiff)
df8.show()
df8.createOrReplaceTempView("table")
spark.sql(
    """
    SELECT Name, IdleDuration, DepartmentName
    FROM table
    WHERE DepartmentName == "Data Engineering" and IdleDuration > 30
    """).show()