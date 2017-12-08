import pymysql
import csv
import datetime
import settings
from mysql import db
import os,time
import pandas as pd
import numpy as np
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date
import csv
import utils
from data_stored import ds

class time_generator(object):
    def __init__(self):
        pass

    def time_main(self, tablename, start_time, end_time):
        db.connect()
        # start_time = str(int(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S'))))
        # end_time = str(int(time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S'))))
        if (int(start_time) + 60) <= int(end_time):

            temp_time = str(int(start_time) + 60)
            while temp_time< end_time:
                filename = utils.getDigitDay(int(start_time)) + '.csv'
                if os.path.isfile(filename) == False:
                    ds.data_to_csv(filename, tablename, start_time, temp_time)
                    start_time = str(int(temp_time) + 1)
                    temp_time = str(int(start_time) + 60)
                    print(filename)
                else:
                    ds.data_to_csv(filename, tablename, start_time, temp_time,1)
                    start_time = str(int(temp_time) + 1)
                    temp_time = str(int(start_time) + 60)
                    print("exist file1")

            else:
                ds.data_to_csv(filename, tablename, start_time, end_time,1)
                print("last read is ok")
        else:
            filename = utils.getDigitDay(int(start_time)) + '.csv'
            if os.path.isfile(filename) == False:
                ds.data_to_csv(filename, tablename, start_time, end_time)
            else:
                ds.data_to_csv(filename, tablename, start_time, end_time,1)
if __name__ == "__main__":
    tablename = 'originData'
    # starttime = '2017-11-6 16:20:20'
    starttime = '1462032202'
    endtime =   '1462032210'
    s =time_generator()
    s.time_main(tablename,starttime,endtime)