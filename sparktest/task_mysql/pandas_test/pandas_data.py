import pandas as pd
import pymysql
import numpy as np
from sqlalchemy import create_engine
# import mysqldb
df = pd.read_csv("sfhd_origin_20160501.csv")
df.head()
print(df.info())
dd = pd.DataFrame(data=df[["time"]]).T
print(dd)
# engine = create_engine('mysql://root:pwd@192.168.1.245/')
host = 'localhost'
port = 3306
db = 'test_mysql'
user = 'root'
password = '1'
# db = pymysql.connect("localhost","root","1","test_mysql")
# cursor = db.cursor()
# df.to_sql('origin_data_pandas',con=db,if_exists='replace',idnex=False)
dba = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, )
sql = "select * from "
df = pd.read_sql(sql,conn=dba,index_col="time")
print(df)
pd.io.sql.to_sql(df,'originDataMonth_test_3',db,flavor='mysql',if_exists='replace',index=False,chunksize=10000)

