import pandas as pd
import numpy as np
from pandas import Series , DataFrame

a = np.random.randn(5)
print(a)

s = Series(a)
print(s)
S = Series(np.random.randn(5),index=['a','b','c','d','e'],name='my_series')
print(S)
print(S.name)

d = {'a':0,'b':1,'c':2}
print(d)
s=Series(d)
print(s)

Series(d,index=['b','c','d','a'])
