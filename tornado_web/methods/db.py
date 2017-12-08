#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host="localhost",user="root",passwd="123",db="test",port=3306,charset="utf-8")
cur = conn.cursor()
