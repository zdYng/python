# import socket,time
# ss = time.time()
# s = socket.socket()
# s.setblocking(0)
# try:
#     s.connect(('www.google.com',80))
# except socket.error as e:
#     print(str(e))
#     i =0
#     while True:
#         try:
#             print("We are connected to %s:%d"%s.getpeername())
#             ee=time.time()
#             print("%s"%(ee-ss))
#             break
#         except:
#             print("Let's do some math while waiting:%d"%i)
#             i+=1
# else:
#     print("!!we are connected to %s:%d"%s.getpeername())
# import socket
# sockets = {}
# for i in range(100):
#     s =socket.socket()
#     sockets[s.fileno()] = s
#     s.setblocking(0)
#     try:
#         s.connect(('www.google.com',80))
#     except:
#         pass
# from greenlet import greenlet
#
# def test1():
#     print(12)
#     gr2.switch()
#     print (34)
#
# def test2():
#     print (56)
#     gr1.switch()
#     print (78)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr2.switch()

import json
import csv
filename = 'sfhd_origin_20160810.csv'
def convert_tojson(data,columns):
    return json.dumps([{'time':i[0],'value':i[1]} for i in data],indent=4)
def read_csv(file):
    csv_rows = []
    with open(file,'rt') as f:
          reader = csv.DictReader(f)
          title = reader.fieldnames
          for row in reader:
              csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
              # break
          return csv_rows
print(type(read_csv(filename)))
# def stored_json(file,data,format=None):
#     with open(file,'wb') as f:
#         if format=="good":
#             f.write(json.dumps(data,sort_keys=False,indent=4,separators=(',',':'),encoding="gbk",ensure_ascii=False))
#         else:
#             f.write(json.dumps(data))
def stored(file,data):
    with open(file,'wb') as f:
        for i in data:
           json.dumps(i,f)

stored("predict_data1.json",read_csv(filename))
# stored_json("predict_data.json",read_csv(filename),'good')
