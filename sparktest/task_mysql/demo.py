import datetime
import settings
from mysql import db
import os, time
from datetime import date
import csv
import utils


def time_main(start_time, end_time, tablename, columns=None):
    timespan = settings.timespan

    db.connect()
    if settings.split_file_number == 0:
        output_filename = 'sfhd_' + utils.getDigitDay(start_time) + '_origin.csv'
    else:
        output_filename = 'sfhd_' + utils.getDigitDay(start_time) + '_origin_' + settings.split_file_number + '.csv'

    # 判断输出文件是否存在 ：False为不存在
    if os.path.isfile(output_filename) == False:
        # 隔一个时间段timespan存一次
        with open(output_filename, 'w') as csvfile:

            if columns == None:
                columns = db.find_columns(tablename)
            data = list(columns)

            writer = csv.writer(csvfile, dialect=("excel"))
            data_1 = sorted(set(data), key=data.index)
            writer.writerow(data_1)

            temp_time = start_time + timespan
            current_time = start_time

            while temp_time <= end_time + 3:
                utils.log_easy('time_main', utils.getTimeDes(temp_time))
                fieldNames, results = db.find(tablename, current_time, temp_time, columns)
                # 插入data
                for info in results:
                    writer.writerow(info)

                current_time = temp_time
                temp_time = current_time + timespan
    db.disconnect()
start_time = 1463500801
end_time = 1463587198
table_name ="originDataMonth_test_3"
time_main(start_time=start_time,end_time=end_time,tablename=table_name)









