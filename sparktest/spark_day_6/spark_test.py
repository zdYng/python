import pyspark,os
from pyspark import SparkConf,SparkContext
os.environ["SPARK_HOME"] = "F:\spark\Spark\spark-2.2.0-bin-hadoop2.7"
sc = SparkContext.getOrCreate()
rdd = sc.parallelize([1,2,3])
print(rdd)
