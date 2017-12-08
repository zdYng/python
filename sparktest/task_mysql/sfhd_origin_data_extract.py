import settings
from mysql import db
import os
import csv
import utils


def time_main(start_time, end_time, tablename, columns=None):

        timespan = settings.timespan
        output_filename = 'sfhd_' + 'origin_' + utils.getDigitDay(start_time) + '.csv'
        db.connect()
        # 判断输出文件是否存在 ：False为不存在
        if os.path.isfile(output_filename) == False:
              pass
        else:
              end_time = start_time
              start_time = start_time -86400
              output_filename = 'sfhd_' + 'origin_' + utils.getDigitDay(start_time) + '.csv'


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

            while temp_time <= end_time+3:
                utils.log_easy('sfhd_origin_data_extract', utils.getTimeDes(temp_time))
                fieldNames, results = db.find(tablename, current_time, temp_time-1, columns)
                # 插入data
                for info in results:
                    writer.writerow(info)
                current_time = temp_time
                temp_time = current_time + timespan
        db.disconnect()

