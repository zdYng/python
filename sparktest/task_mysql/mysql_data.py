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


    # def read_csv_datas(self,filename):
    #
    #     #读取文件datas
    #     f = open(filename, 'r')
    #     datas = []
    #     for row in csv.reader(f):
    #         datas.append(row)
    #     f.close()
    #     return datas
    # def read_csv_para(self,filename):
    #     #读取列名
    #     params = pd.read_csv(filename, encoding="gbk", nrows=1)
    #     #返回列名,列datas
    #     buffer=[]
    #     t= 0
    #     for p in params:
    #         t+=1
    #     #将取出来的params存到list里去
    #     try:
    #         for row in params:
    #             buffer.append(row)
    #     except Exception as e:
    #         print(e)
    #     del buffer[0]
    def test(self):
        print("OK!")





    #取出的数据存到mysql的表中
    def read_frame(self,filename,tablename):

        # 读取文件datas
        f = pd.read_csv(filename,encoding="gbk",skiprows=1)
        datas = []
        for row in f:
            datas.append(row)

        # 读取列名
        params = pd.read_csv(filename, encoding="gbk", nrows=1)
        # 返回列名,列datas
        columns = []
        t = 0
        for p in params:
            t += 1
        # 将取出来的params存到list里去
        try:
            for row in params:
                columns.append(row)
        except Exception as e:
            print(e)
        del columns[0]
        #连接数据库
        mysql.connect(self)
        #判断表是否存在
        try:
           res= mysql.is_table_exist(self,tablename=tablename,dbname=settings.database)
           #创建表

           if  res==None :
               mysql.create_table(self,tablename=tablename,columns=columns,spec='time')
               print("Create table is ok!")
           else:
               return "table is exist"
        except  Exception as e:
            print("Unexpected Error: {}".format(e))


        #插入数据
        mysql.insert_mysql_with_json(self,tablename=tablename,datas=datas)
        return print("insert is ok!!!\n")

    #存储的time 数字化

    def time_toNum(self,data_times):
        """


        :param data_times:
        :return:
        """
        datas=[]
        for time_o in data_times:
            st = time.strptime(time_o,'%Y-%m-%d %H:%M:%S')
            datas.append(time.mktime(st))

        return datas

    #将数字化的time存到mysql的表里

    def timeNum_storage(self,data_times,tablename,datas):

        datas = self.time_toNum(data_times)
        mysql.insert_mysql_with_json(self,tablename=tablename,datas=datas)

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
        # sched.add_job(func, 'date', run_date=need_time, args=['text'])
        # sched.add_job(func,args=['text'])
        sched.start()

if __name__ =="__main__":
    s = mysql_data()
    s.getPrimetime(s.test(),1)



