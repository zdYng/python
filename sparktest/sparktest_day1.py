import pandas
from pyspark import SparkContext

file = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
import pandas as pd
import os
df = pd.read_csv(file,header=None)
print(df.head(10))


