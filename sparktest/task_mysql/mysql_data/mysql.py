# -*- coding: utf-8 -*-
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

        self.insert_into_sql(ret)
        print("1")
    def insert_into_sql(self,sqls):
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

db = mysql()
