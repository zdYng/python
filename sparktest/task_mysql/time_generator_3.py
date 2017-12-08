import pymysql
import csv
import datetime
import settings
from mysql import db
import os,time
from datetime import date
import csv
import utils
from data_stored import ds

class time_generator(object):
    def __init__(self):
        pass

    def time_main(self,start_time,end_time,tablename,columns=None):
        # tablename = settings.tablename
        # start_time =str(settings.start_time)
        # end_time = str(settings.end_time)
        timespan =settings.timespan

        db.connect()
        if settings.split_file_number ==0:
           output_filename = 'sfhd_'+utils.getDigitDay(int(start_time)) + '_origin.csv'
        else :
            output_filename = 'sfhd_' + utils.getDigitDay(int(start_time)) + '_origin_'+settings.split_file_number+'.csv'

        #判断输出文件是否存在 ：False为不存在
        if os.path.isfile(output_filename) == False:
            #隔一个时间段timespan存一次
            csvfile = open(output_filename, 'w')
            fieldNames, results = db.find(tablename, start_time, end_time,columns)
            data = []
            for fn in fieldNames:
                data.append(fn)
            writer = csv.writer(csvfile, dialect=("excel"))
            data_1 = sorted(set(data), key=data.index)
            writer.writerow(data_1)

            temp_time = str(int(start_time) + timespan)
            current_time = str(start_time)

            while temp_time <= str(int(end_time)+3):
                 print(utils.log_easy())
                 # ds.data_to_csv(output_filename, tablename, current_time, temp_time)
                 fieldNames, results = db.find(tablename, current_time, temp_time,columns)
                 # 插入data
                 for info in results:
                     writer.writerow(info)

                 current_time = str(temp_time)
                 temp_time  = str(int(current_time) + timespan)

                 # print('ok...')

        csvfile.close()
        db.disconnect()

            # return None


            # return None




# if __name__ == "__main__":
#     test = time_generator()
#     test.time_main()

tg = time_generator()


