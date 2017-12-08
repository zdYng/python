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

    def get_filename(self,sec=None):
        if sec is None:
            sec = time.time()
        tplSec = time.localtime(int(sec))
        return '%4d-%02d-%02d_%02d:%02d' % tuple(tplSec[:5])

    def time_main(self,tablename,start_time,end_time):
        db.connect()
        #判断时间段长度
        if (int(start_time)+60)<=int(end_time):
            temp_time = str(int(start_time)+60)
            while temp_time < end_time:
                filename=self.get_filename(start_time)+'.csv'
             # filename = utils.getDigitDay(int(start_time)) + '.csv'
                if os.path.isfile(filename)==False:
                    ds.data_to_csv(filename,tablename,start_time,temp_time)
                    start_time = str(int(temp_time) + 1)
                    temp_time = str(int(start_time) + 60)
                    print(filename)
                else:
                    start_time = str(int(temp_time) + 1)
                    temp_time = str(int(start_time) + 60)
                    print("exist file1")
                    pass


            else:

                # start_time = str(int(temp_time) + 1)
                filename = self.get_filename(start_time) + '.csv'
                if os.path.isfile(filename) == False:
                    # filename = utils.getDigitDay(int(start_time)) + '.csv'
                    ds.data_to_csv(filename, tablename, start_time, end_time)
                    print(filename)
                    return None
                else:

                    print("exist file2")
                    return None
        else:
            filename = self.get_filename(start_time) + '.csv'
            if os.path.isfile(filename)==False:
                ds.data_to_csv(filename, tablename, start_time, end_time)
                print(filename)
            else:
                print("exist 3")
                pass






if __name__ == "__main__":
    tablename = 'originData'
    starttime = '1462032001'
    endtime =   '1462032004'
    s =time_generator()


    s.time_main(tablename,starttime,endtime)
    # for field in fieldNames:
    #     print(field)
    # for r in results:
    #     print(r)


