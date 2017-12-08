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
import re
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date
import csv
table_name ="test1"
db.connect()
file_name = "sfhd_origin_20160501.csv"
t = re.sub("\D","",file_name)
print(t)
st = t[0:4]+"-"+t[4:6]+"-"+t[6:]+" 00:00:00"
print(st)
et = t[0:4]+"-"+t[4:6]+"-"+t[6:]+" 23:59:59"
print(et)
#
# st = t + " 00:00:00"
# print(st)
#
# et = t + " 23:59:59"
# print(et)

# csvfile = open(file_name, 'r')
# dict_reader = csv.DictReader(csvfile)
# datas = []
# freq = 0
# # for row in dict_reader:
#     row = dict(row)
#     columns = []
#     t=0
#     for i in row.keys():
#         t+=1
#         columns.append(i)
#         print(t)
#     if (db.is_table_exist(table_name, settings.database) == None and freq == 0):
#         db.create_table(table_name, columns)
#         freq += 1
#         print("create is ok")
#     else:
#         # print("existed!")
#         pass
#     break



# db.creat_table(table_name,columns)