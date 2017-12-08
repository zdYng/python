import settings
from mysql import db
import os
import csv
import utils


def time_main(start_time, end_time, tablename, columns=None):
    db.connect()
    timespan = settings.timespan
    cur_time = start_time - 86400*10

    while cur_time < end_time:
        next_time = cur_time + 86400


        # 判断输出文件是否存在 ：False为不存在
        if os.path.isfile('sfhd_' + 'origin_' + utils.getDigitDay(cur_time) + '.csv') == False:
              output_filename = 'sfhd_' + 'origin_' + utils.getDigitDay(cur_time) + '.csv'

        else:
              print("%s 文件存在" % utils.getDigitDay(cur_time))
              cur_time = next_time

              continue


        # 隔一个时间段timespan存一次
        with open(output_filename, 'w') as csvfile:

            if columns == None:
                columns = db.find_columns(tablename)
            data = list(columns)
            print(data)

            writer = csv.writer(csvfile, dialect=("excel"))
            data_1 = sorted(set(data), key=data.index)
            writer.writerow(data_1)
            current_time = cur_time
            row = 0
            while current_time <  next_time :
                temp_time = current_time + timespan
                utils.log_easy('sfhd_origin_data_extract', utils.getTimeDes(temp_time))
                fieldNames, results = db.find(tablename, current_time, temp_time-1, columns)
                # 插入data
                for info in results:
                    writer.writerow(info)
                    row+=1
                current_time = temp_time
            print("插入行数为：%i"%row)
        cur_time = next_time

    db.disconnect()

