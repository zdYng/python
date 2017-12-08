from  mysql import db
import settings
import pymysql

data = [{'time':123321,'predict':1.222},{'time':123322,'predict':1.223},{'time':123324,'predict':1.213}]
col =[]
# for i in data:
#     #获取列名
#     for ii in i.keys():
#         col.append(ii)
#     break
# print(col)
#
# #  data = {(time:123, predic:1.22) }
# #  datas:字典{(key: value),.....}
# # for i in data:
# #     del i['time']
# # print(data)
# cols = []
# for da in data:
#     for ii in da.keys():
#         cols.append(ii)
#     break
#
# print(len(cols))
for da in data:
    # print(da)
    print(da['time'])
print(len(da.keys()))