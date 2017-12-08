# # -*- coding: UTF-8 -*-
import utils
t1 = utils.getTimeSec("2017-11-17 16:40:00")
t2 = utils.getTimeSec("2016-07-04 00:00:00")
print(t1, t2, t1-t2)
# import time
# import sys
# import binascii
# import uuid
# import socket
# import struct
# import os
# import math
# import decorator
# import shutil
#
# split = ''
#
# LOG_INTERVAL = 5
# class utils_py3(object):
#   def __init__(self):
#
#       # def getNow(self):
#       #     return int(time.time())
#       #
#       # def getDateSec(self,desc):
#       #     time_local = time.strptime(desc, '%Y%m%d')
#       #     return int(time.mktime(time_local))
#       pass
#
#   def getHMSec(desc):
#       time_local = time.strptime(desc, '%H:%M')
#       return time_local.tm_hour * 3600 + time_local.tm_min * 60
#
#   def getDateSec(self,desc):
#           time_local = time.strptime(desc, '%Y%m%d')
#           return int(time.mktime(time_local))
#   def getNow(self):
#        return int(time.time())
#   #001
#
#   def getTimeDes(self,sec=None):
#       if sec is None:
#         sec = int(time.time())
#       else:
#         pass
#       tplSec = time.localtime(sec)
#       print('tplSec:',tplSec)
#
#       return  time.strftime('%Y-%m-%d %X',tplSec)
#       #返回值为 ：2017-11-02 19:20:08
#   #002
#
#   def getTimeDay(self,sec=None):
#       if sec is None:
#           sec = int(time.time())
#       tplSec = time.localtime(sec)
#       return '%04d-%02d-%02d' %tplSec[:3]
#       #返回值：2017-11-02
#   #003
#   def getTimeSec(self,desc):
#       if isinstance(desc,int):
#           desc = str(desc)
#       if len(desc) == 0:
#           return self.getNow()
#       if len(desc) <= 10:
#           return self.getDateSec(desc)
#       if desc.count('-') == 1:
#           time_local = time.strptime(desc,'%Y%m%d-%H:%M:%S')
#       elif desc.count('-') == 2:
#           time_local = time.strptime(desc,'%Y-%m-%d %H:%M:%S')
#       return int(time.mktime(time_local))
#
#   class Logger(object):
#     def __init__(self):
#         self.lastPrintTime = 0
#         self.log_file = None
#
#     def _set_log_file(self,filename):
#         self.log_file = open(filename,'w')
#
#     def _reset_log_file(self,):
#         if self.log_file:
#             self.log_file.close()
#         self.log_file = None
#
#     def _print(self,msg):
#         info = '%s : %s' %(self.getTimeDes(),msg)
#
#
#
#
#
# if __name__ == "__main__":
#
#     test = utils_py3()
#     # sec = int(time.mktime(time.strptime(time.time(),'%Y%m%d')))
#     sec = '2017-11-02 20:23:37'
#     sec2 = ''
#     sec3 ='20171102'
#     sec4 = '20171102-20:23:37'
#     sec5 = 1509625923
#     # print(sec)
#     #001
#     print(test.getTimeDes())
#     #002
#     print(test.getTimeDay())
#     #003
#     print(test.getTimeSec(sec))
#     print(test.getTimeSec(sec2))
#     print(test.getTimeSec(sec3))
#     print(test.getTimeSec(sec4))
#     print(test.getTimeSec(sec5))
#     #4
#     msg='1'
#     logs = test.Logger()
#     print(logs._print(msg))
#
