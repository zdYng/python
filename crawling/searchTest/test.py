import MySQLdb
print MySQLdb

conn = MySQLdb.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='qzd123321',
    db='booknovel',
    charset='gbk'
)
cursor =conn.cursor()

cursor.close()
conn.close()