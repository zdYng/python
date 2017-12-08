# -*- coding: utf-8 -*-
import settings
from mysql import db
import os, time
import csv
import re
import sfhd_origin_data_extract
class data_to_mysql():
    def __init__(self):
        pass



    def get_time(self, file_name):
        # file_name = "sfhd_origin_20160501.csv"
        t = re.sub("\D", "", file_name)
        print(t)
        s = t[0:4] + "-" + t[4:6] + "-" + t[6:] + " 00:00:00"
        st = int(time.mktime(time.strptime(s, "%Y-%m-%d %H:%M:%S")))
        # print(st)
        e = t[0:4] + "-" + t[4:6] + "-" + t[6:] + " 23:59:59"
        et = int(time.mktime(time.strptime(e, "%Y-%m-%d %H:%M:%S")))
        # print(et)
        #返回类型为 INT 类型
        return st, et

    # 将数据存到mysql中的方法
    def data_stored_mysql(self, file_name, table_name):
        csvfile = open(file_name, 'r')
        dict_reader = csv.DictReader(csvfile)
        db.connect()
        datas = []
        freq = 0
        for row in dict_reader:
            row = dict(row)
            # 创建表
            columns = []
            for i in row.keys():
                columns.append(i)
            if (db.is_table_exist(table_name, settings.database) == None and freq == 0):
                db.create_table(table_name, columns)
                freq += 1
                print("create is ok")
            else:
                pass
                # 插入数据
            # row['time'] = int(time.mktime(time.strptime(row['time'], '%Y-%m-%d %H:%M:%S')))
            row['time'] = int(row['time'])
            datas.append(row)
        db.insert_mysql_with_json(table_name, datas)
        print("insert is ok")
        db.disconnect()

    # 文件存到 mysql
    def main_storeto_mysql(self, file_dir, table_name):
        file_names = []
        for root, dirs, files in os.walk(file_dir):
            fs = time.time()
            # i = 1
            for f in files:
                # if i <= 3 :
                fs_1 = time.time()
                file = "/home/grid/sparktest/task_mysql/sfhd_origin_data/" + f
                #调用函数data_stored_mysql 存数据到mysql
                self.data_stored_mysql(file, table_name)
                fs_2 = time.time()
                print("%s文件存储,消耗时间:%s " % (f, fs_2 - fs_1))
                # i+=1

            fe = time.time()
            print("存储mysql总消耗时间：", fe - fs)
            # pass

    def main_storeto_CSV(self, file_dir, table_name):

        for root, dirs, files in os.walk(file_dir):

            fs = time.time()
            # i =1

            for file in files:
                # if i <= 3:
                fe_1 = time.time()
                st, et = self.get_time(file)
                print(st, et)
                sfhd_origin_data_extract.time_main(st, et, table_name)
                fe_2 = time.time()

                print("存储%s消耗时间：%s" % (file, fe_2 - fe_1))
                # i+=1
                # print(i)
                # 存三次

            fe = time.time()
            print("存储csv结束时间：", (fe - fs))


if __name__ == "__main__":
    table_name = "originDataMonth_test_11_13"
    dtm = data_to_mysql()
    # dtm.main_storeto_mysql("/home/grid/sparktest/task_mysql/sfhd_origin_data", table_name)
    dtm.main_storeto_CSV("/home/grid/sparktest/task_mysql/sfhd_origin_data", table_name)