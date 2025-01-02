from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

def sparktut():
    spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial").config("spark.memory.offHeap.enabled","true").config("spark.memory.offHeap.size","10g").getOrCreate()
    spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")
    df = spark.read.csv('data.csv', header = True, escape="\"")
    df = df.withColumn('date', to_timestamp("InvoiceDate", 'MM/dd/yy HH:mm'))
    df.show(5, 0)
    print(df.count())
    print(df.select('CustomerID').distinct().count())
    print(df.groupBy('Country').agg(countDistinct('CustomerID').alias('country_count')).orderBy(desc('country_count')).show())
    print('max date is')
    df.select(max("date")).show()
    print('min date is')
    df.select(min("date")).show()
    min_date = df.select(min("date")).collect()[0][0]
    print(min_date)
    df = df.withColumn('from_date', lit(min_date))
    df.show(5, 0)
    df2 = df.withColumn('recency', col("date").cast("long") - col('from_date').cast("long"))
    df2.show(5, 0)



if __name__ == "__main__":
    sparktut()