# -*- coding: utf-8 -*-
import pymysql
import csv
import settings
from mysql import mysql
import os,time
import pandas as pd
import numpy as np
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date
# ip="localhost"
# mysql_user="hive"
# mysql_passwd="hive"
# database="spark_kafka_test"

class mysql_data(object):
    def __init__(self):
        self.db =mysql()
        self.dbname = settings.database
    #取出的数据存到mysql的表中
    def read_frame(self,filename,tablename):
        mysql.connect(self)
        print("Connect is Ok")


        data=  pd.read_csv(filename,nrows=1,encoding="gbk")
        dat=[]
        # for d in data.columns:
        #     dat.append(d)
        # del dat[0]
        #判断第一列第一行是否为'time'
        num =1
        for d in data.columns:
            if (d!='time'and num==1):
                num+=1
                pass
            elif num >1:
                dat.append(d)
        #create key
        if mysql.is_table_exist(self,tablename=tablename,dbname=settings.database)==None:
          mysql.create_table(self,tablename=tablename,columns=dat,spec='time_num' )
          # print("Creat Ok")
        else:
            print("table is existed!")

        f = pd.read_csv(filename,encoding="gbk")
        ret = []
        n=1
        for y in dat:
            for x in f.ix[0:,y]:
                sql = "insert into %s %s value %s" %(tablename,y,x)
                print(n)
                n+=1
                ret.append(sql)
                # break
            # sql_timenum = "insert into %s %s value %s "%tablename,timenum,data_num
            # ret.append(sql_timenum)
            mysql.insert_into_sql(self,sqls=ret)
            print("insert %s is ok"%y)

            break
    # #存储的time 数字化
    #
    # def time_toNum(self,data_times):
    #     """
    #
    #
    #     :param data_times:
    #     :return:
    #     """
    #     datas=[]
    #     for time_o in data_times:
    #         st = time.strptime(time_o,'%Y-%m-%d %H:%M:%S')
    #         datas.append(time.mktime(st))
    #
    #     return datas
    #
    # #将数字化的time存到mysql的表里
    #
    # def timeNum_storage(self,data_times,tablename,datas):
    #
    #     datas = self.time_toNum(data_times)
    #     # mysql.insert_mysql_with_json(self,tablename=tablename,datas=datas)

    def time_num_stored(self,tablename,filename):
        # 时间戳
        filename = 'may_origin.csv'
        f = pd.read_csv(filename, encoding='gbk')
        data = []
        for d in f.ix[0:, 1]:
            data.append(d)
        datas = []
        for time_o in data:
            st = time.strptime(time_o, '%Y-%m-%d %H:%M:%S')
            datas.append(time.mktime(st))
        # print(datas)
        #store to mysql
        ret = []
        cursor = mysql.cursor()
        sql = "alter table tablename add primary key(time_num) INT not null "
        for dt in datas:
            sql2 = "insert into %s time_num value %s" % tablename, dt
            ret.append(sql2)
        mysql.insert_into_sql(ret)


    #查找start_time 到End_time 的数据,并存到单独的.csv文件中
    def find_StimeToEtime(self,tablename,start_time,end_time,New_file_name):
        """


        :param tablename:
        :param start_time:
        :param end_time:
        :param New_file_name:
        :return:
        """
        # 所有列名
        columns = mysql.find_columns(tablename)
        #查找
        fieldName,results = mysql.find(tablename=tablename,start_time=start_time,end_time=end_time,fieldName=None)
        #存到.csv
        write= csv.writer(open(New_file_name,'wb'),dialect='excel')
        write.writerows(columns)
        write.writerows(results)
        # print("存储....ok")

    #定时函数
    def getPrimetime(self,func,num):


        sched = BlockingScheduler()
        # sched.add_job(func, 'date',run_date=date(year,month,day),args=['text'])
        if num ==1:
           year = int(input('year: '))
           month = int(input('month: '))
           day = int(input('day: '))
           hour = int(input('hour: '))
           minute = int(input('minute: '))
           second = int(input('second: '))
           #特定的时间
           need_time= sched.add_job(func, 'date', run_date=date(year, month, day,hour,minute,second), args=['text'])
        else :
            #当前时间
            need_time =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        sched.add_job(func, 'date', run_date=need_time, args=['text'])
        sched.add_job(func,args=['text'])
        sched.start()

if __name__ == "__main__":
    t = mysql_data()
    t.read_frame(filename= 'may_origin.csv',tablename= 'origin_data')





