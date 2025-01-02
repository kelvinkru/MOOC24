from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler

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
    df2 = df2.join(df2.groupBy('CustomerID').agg(max('recency').alias('recency')), on='recency', how='leftsemi')
    df2.show(20, 0)
    df_freq = df2.groupBy('CustomerID').agg(count('InvoiceDate').alias('frequency'))
    df_freq.show(5, 0)
    df3 = df2.join(df_freq, on='CustomerID', how='inner')
    df3.show(5, 0)
    m_val = df3.withColumn('TotalAmount', col("Quantity")*col("UnitPrice"))
    m_val = m_val.groupBy('CustomerID').agg(sum('TotalAmount').alias('monetary_value'))
    finaldf = m_val.join(df3, on='CustomerID', how='inner')
    finaldf = finaldf.select(['recency','frequency','monetary_value','CustomerID']).distinct()
    finaldf.show(20)

    assemble = VectorAssembler(inputCols=[
        'recency', 'frequency', 'monetary_value'
    ], outputCol='features')

    assembled_data = assemble.transform(finaldf)
    scale = StandardScaler(inputCol='features', outputCol='standardized')
    data_scale = scale.fit(assembled_data)
    data_scaled_output = data_scale.transform(assembled_data)
    data_scaled_output.select('standardized').show(20, 0)



if __name__ == "__main__":
    sparktut()