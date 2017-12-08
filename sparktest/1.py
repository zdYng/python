import os
from pyspark import SparkConf
os.environ["SPARK_HOME"] = "F:\spark\Spark\spark-2.2.0-bin-hadoop2.7"
conf = (SparkConf().setMaster('local').setAppName('a'))