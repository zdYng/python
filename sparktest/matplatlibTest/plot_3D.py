file = "F:\\learnPython\\sparktest\\csv_data_task01\\ANAHIST0_2.csv"
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(file,encoding="gbk")
M = df.iloc[0:100,[5,9]].values
# print(M)
plt.scatter(M[:50,0],M[:50,1],color='red',marker='o',label='setosa')
plt.scatter(M[50:100,0],M[50:100,1],color='blue',marker='x',label='versicolor')
plt.xlabel('40LCH2DC.AV')
plt.xlabel('40LCH3DC.AV')
plt.legend(loc='upper left')
plt.show()