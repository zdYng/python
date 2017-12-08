# coding : utf-8
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port = 3306,
    user = 'root',
    passwd ='',
    db='test',
)
cur = conn.cursor()


# cur.execute("create table students(id int,name varchar(20),class varchar(30),age varchar(10))")


cur.execute("insert into students values('2','Tom','3Y2C','9')")
cur.execute("insert into students values('3','Alen','3Y3C','9')")


cur.execute("update students set class='3Y1C' where name ='Tom'")








cur.close()
conn.commit()
conn.close()