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
import utils
# filename = 'may_origin.csv'
# tablename = 'origin_data'
class data_stored(object):
    def __init__(self):
        pass


    def data_stored(self,filename,tablename):

        csvfile = open(filename,'r')
        dict_reader = csv.DictReader(csvfile)
        db.connect()
        datas = []
        freq = 0

        for row in dict_reader:
             row = dict(row)
             if row['']:
                del(row[''])
     #创建表
             columns =[]
             for i in row.keys():
                  columns.append(i)
             if (db.is_table_exist(tablename=tablename,dbname=settings.database) ==None and freq ==0 ):
                    db.create_table(tablename=tablename,columns=columns)
                    freq += 1
                    print("create is ok")
             else:
                  pass
    #插入数据
             row['time'] = int(time.mktime(time.strptime(row['time'], '%Y-%m-%d %H:%M:%S')))
             datas.append(row)
        db.insert_mysql_with_json(tablename, datas)
        print("insert is ok")
        db.disconnect()

    def data_to_csv(self,filename,tablename,starttime,endtime,readfile=None,sep=None):

        db.connect()
        fieldNames, results = db.find(tablename, starttime, endtime)


        data = []

        for fn in fieldNames:
            data.append(fn)
        #文件不存在
        if readfile == None:
           csvfile = open(filename, 'w')
           writer = csv.writer(csvfile, dialect=("excel"))
           # 插入列名
           data_1 = []
           data_1 = sorted(set(data), key=data.index)
           writer.writerow(data_1)
        #文件存在
        else:
            csvfile = open(filename, 'a')
            writer = csv.writer(csvfile, dialect=("excel"))

        # 插入data
        for info in results:
            data_2 = []
            # for m_2 in info:
            #     data_2.append(m_2)
            writer.writerow(info)
        csvfile.close()
        db.disconnect()
# #
# if __name__ == "__main__":
#     filename='may_origin.csv'
#     filename2='csvtest_05.csv'
#     tablename = 'originData'
#     st = 1462032004
#     et = 1462032007
#
#     t = data_stored()
#     starttime = datetime.datetime.now()
#
#     # t.data_stored(filename,tablename)
#     t.data_to_csv(filename2,tablename, st,et)
#     endtime =datetime.datetime.now()
#
#     print(endtime-starttime)
ds = data_stored()
