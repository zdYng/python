# -*- coding:utf-8 -*-
import pymysql
import settings

class mysql(object):
    def __init__(self):
        self.db = None

    def connect(self):

          self.db = pymysql.connect(host=settings.ip, port=settings.port, user=settings.mysql_user, passwd=settings.mysql_passwd, db=settings.database, )
          print("connect is ok")
          # return 1
    def disconnect(self):
        self.db.close()
        # return -1

    def create_table(self, tablename, columns, spec='time'):
        """
        :param tablename:
        :param spec:
        :param columns: 列表[]
        :return:
        """

        type_data = ['int', 'double(10,3)']
        cursor = self.db.cursor()
        sql="create table %s("%(tablename,)
        sqls=[]
        for col in columns:
            #判断是否time_num
            if col==spec:
                sqls.append('%s %s primary key'%(col,type_data[0]))
            else:
                sqls.append('%s %s'%(col,type_data[1]))

        sqlStr = ','.join(sqls)
        sql+=sqlStr+')'
        try:
            cursor.execute(sql)
            print("Table %s is created"%tablename)
        except:
            self.db.rollback()

    def is_table_exist(self, tablename,dbname):
        cursor=self.db.cursor()
        sql="select table_name from information_schema.TABLES where table_schema='%s' and table_name = '%s'"%(dbname,tablename)
        #results="error:Thie table is not exit"
        try:
            cursor.execute(sql)

            results = cursor.fetchall() #接受全部返回行
        except:
            #不存在这张表返回错误提示
             raise Exception('This table does not exist')
        if not results:
             return None
        else :
            return results
    # print datas
    def insert_mysql_with_json(self, tablename, datas):
        """

        :param tablename:
        :param datas:字典{(key: value),.....}
        :return:
        """
        # keys = datas[0]
        keys = datas[0].keys()
        keys = str(tuple(keys))
        keys = ''.join(keys.split("'")) # 用' 隔开
        print(keys)
        ret = []
        for dt in datas:
            values = dt.values()   ##      ‘str’ object has no attribute#
            sql = "insert into %s" % tablename + keys
            sql = sql + " values" + str(tuple(values))
            ret.append(sql)
            # print("1")
        # print keys  insert into %tablename dat[i]  values str[i]

        self.execute_sql(ret)
        print("1")
    def execute_sql(self,sqls):
        cursor = self.db.cursor()
        for sql in sqls:
            # 执行sql语句
            try:
                cursor.execute(sql)
                self.db.commit()
                # print("insert %s" % sql, "success.")
            except:
                # Rollback in case there is any error
                self.db.rollback()
    #找列名
    def find_columns(self, tablename):
        sql = "select COLUMN_NAME from information_schema.columns where table_name='%s'" % tablename
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            raise Exception('hello')
        return tuple(map(lambda x: x[0], results))

    def find(self, tablename, start_time, end_time, fieldName=None):
        """
        :param tablename: test_scale1015
        :param fieldName: None or (columns1010, columns1011, columns1012, columns1013, time)
        :return:
        """
        cursor = self.db.cursor()
        sql = ''
        if fieldName==None:
            fieldName = self.find_columns(tablename)
            sql = "select * from %s where time between %s and %s" % (tablename, str(start_time), str(end_time))
            # print('None')
        else:
            fieldNameStr = ','.join(fieldName)
            sql = "select %s from %s where time between  %s and %s" % (
            fieldNameStr, tablename, str(start_time), str(end_time))
            # print('sm')
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            raise Exception('hello')
        return fieldName, results,

    def update(self,datas, tablename):
        cursor = self.db.cursor()
        columns = []
        for data in datas:
            for i in data.keys():
                columns.append(i)
            #取出key值，且只循环一次就break
            break
        if len(columns)>=2:
            # columns_2=columns[:]
           # db.connect()
            if db.is_table_exist(tablename, settings.database):
                # exists
                # pass
                for col in columns:
                    if col != 'time':
                        sql = "alter table %s add column %s double(10,3);" % (tablename, col)
                        try:
                            cursor.execute(sql)
                            print("%s is altered ok" % (col))
                        except:
                            print("alter is failed")
                    else:
                        # pass
                        for data in datas:
                            sql ="select * from `%s` where time=%s"%(tablename,data['time'])
                            if cursor.execute(sql) ==0:
                                #不存在
                                cursor.execute("insert into %s (time) values ('%s')" % (tablename, data['time']))
                                print("time 不存在并插入")
                                import time
                                # time.sleep(0.0001)
                 #更新
                ret = []
                for data_1 in datas:
                    col = []
                    for data_2 in data_1.keys():
                        col.append(data_2)
                    #  time = col[0]  and  predict = col[1]
                    #判断time是否在第一列
                    if col[0]=="time":
                        time_data = data_1[col[0]]
                        predic_data = data_1[col[1]]
                        sql = "update %s set %s='%s'where %s=%s" % (tablename, col[1], predic_data, col[0], time_data)
                        #   update tablename set predict='predict_data' where time=time_data
                    else:
                        time_data = data_1[col[1]]
                        predic_data = data_1[col[0]]

                        sql = "update %s set %s='%s'where %s=%s"%(tablename,col[0],predic_data,col[1],time_data)
                    print("update yes")
                    ret.append(sql)
                self.execute_sql(ret)

                # db.insert_mysql_with_json(tablename, datas)
            else:
                # table is no exists
                db.create_table(tablename, columns)
                db.insert_mysql_with_json(tablename, datas)
        else:
            print("data 需要有2列数据 如[{'time':123321,'predict':1.222}]")

db = mysql()
# data = [{'time':123321,'predict':1.222},{'time':123322,'predict':1.223},{'time':123324,'predict':1.213}]
# data2 = [{'time':123321,'predict2':1.224},{'time':123322,'predict2':1.225},{'time':123324,'predict2':1.216}]
# data3 = [{'time':123321,'predict3':1.221},{'time':123322,'predict3':1.222},{'time':123324,'predict3':1.226}]
# data4 = [{'time':1231324,'predict6':1.221},{'time':125678,'predict6':1.222},{'time':1234569,'predict6':1.226}]
# data6 =[{'time':213,'pre':1.223}]
# data7 =[{'time':214,'pre':1.224}]
# db.connect()
#
# db.updata(data4,settings.tablename_2)
# from mysql import db

db.connect()
db.update([{'time':144, 'columns3':132}], 'test_update')
print(db.find('test_update', 0,1000))
db.disconnect()