
import os
import pandas as pd

p = pd.read_csv("F:\\learnPython\\sparktest\\csv_data_task01\\parameters_final.csv",encoding="gbk")
p_av = list(map(lambda x : x + '.AV',list(p["Parameters"])))
df = pd.DataFrame()
#read F_2 F_6
f_2 = pd.read_csv("F:\\learnPython\\sparktest\\csv_data_task01\\ANAHIST0_2.csv",encoding="gbk")
f_6 = pd.read_csv("F:\\learnPython\\sparktest\\csv_data_task01\\ANAHIST0_6.csv",encoding="gbk")
#将汉字部分改为time
f_2.rename(columns= lambda  x : x.replace(u'时间/点名','time'),inplace=True)
f_6.rename(columns= lambda  x : x.replace(u'时间/点名','time'),inplace=True)

#inter
inter_2 = list(set(f_2.columns).intersection(set(p_av)))
inter_6 = list(set(f_6.columns).intersection(set(p_av)))

for count in range(144):
    pF_2=f_2[inter_2]
    pF_2.insert(0,'time','0:00:'+f_2.time)
    pF_6=f_6[inter_6]
    pF_6.insert(0,'time','0:00:'+f_6.time)
    mix = pd.merge(pF_2,pF_6,on='time')
    df = pd.concat([df,mix])
print(df)


