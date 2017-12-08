# -*- coding:utf-8 -*-
# 存数据到mysql (只存了时间数字）
import pymysql
import csv
import datetime
import settings
from mysql import db
import os,time
import pandas as pd
import numpy as np
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date
import csv
db.connect()
fieldNames ,results= db.find('originData','1462032115','1462032124')
# print(type(fieldNames),type(results))
data_1 = []
data_2 = []
for fn in fieldNames:
    data_1.append(fn)

csvfile = open('csvtest1.csv','w')
writer = csv.writer(csvfile,dialect=("excel"))
#插入列名
writer.writerow(data_1)
#插入data
for info in results:
    x= []
    for m_2 in info:
       x.append(m_2)
    writer.writerow(info)
csvfile.close()

