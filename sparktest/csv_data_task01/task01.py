import csv
import os
#存数据
Data = []
f=open("F:\learnPython\sparktest\csv_data_task01\parameters_final.csv","r",encoding='gbk')
reader = csv.reader(f)
param = []
#读取final.csv 的key
for column in reader:
    param.append(column[0])
    print(param)

fileHeader = ['time']
for i in param[1:]:
    fileHeader.append(i)
print(fileHeader)

targetFile = open("F:\learnPython\sparktest\csv_data_task01\tenminutes.csv",'w',encoding='gbk')
writer = csv.writer(targetFile)
writer.writerow(fileHeader)
targetFile.close()

f = open('F:\learnPython\sparktest\csv_data_task01\ANAHIST0_2.csv','r',encoding='gbk')
reader = csv.reader(f)
time = [row[0] for  row in reader]
time = time[1::3]   # 3s qu一次
Data.append(time)

def Searcher(param):
    param2 = ''+param + '.AV'
    f2 = open('F:\learnPython\sparktest\csv_data_task01\ANAHIST0_2.csv','r',encoding='gbk')
    dicreader2 = csv.DictReader(f2)
    column2 = [row.get(param2) for row in dicreader2]
    if column2[0] == None:
        f2.close()
        f6 = open('F:\learnPython\sparktest\csv_data_task01\ANAHIST0_6.csv','r',encoding='gbk')
        dicreader6 = csv.DictReader(f6)
        column6 = [row.get(param2) for row in dicreader6]
        if column[0]!=None:
            Data.append(column6)
        f6.close()
    else:
        column6 = column2[::3]
        Data.append(column6)
        f2.close()

for it in param:
    Searcher(it)

l = zip(*Data)
new_Data = list(map(str,1))
for result in new_Data:
    print(result)

targetFile = open("F:\learnPython\sparktest\csv_data_task01\tenminutes.csv",'a',encoding='gbk')
addwriter = csv.writer(targetFile)
addwriter.writerows(new_Data)
# print(targetFile.text)
targetFile.close()


