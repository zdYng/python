# -*- coding: utf-8 -*-
import requests
import urllib2
import os
from mmtaobao.cons import headers
from lxml import etree
from parsel import Selector

import datetime
# html =requests.get("http://cl.j4q.pw/htm_data/2/1709/2664390.html")
# html.encoding = 'utf-8'
# #print html.text
# select = etree.HTML(html.text)
#
# #print select
# content =select.xpath('//table//div//img/@src')
#
# print content
#

for x in range [1,50]:
 c="http://imgwe.com/i2/ti%s.jpg" %x
 os.chdir(r"D://pic")
 req = urllib2.Request(c)
 req.add_header('User-agent', headers())
       # html = urllib2.urlopen(req).read()
 response =urllib2.urlopen(req)
 f = open('%s.jpg'%x,'wb')
 f.write(response.read())
 print x
 f.close()

# for imgurl in content:
#
#     x=datetime.datetime.now()
#
#     name = imgurl[-12:]
#     os.chdir(r"D://pic")
#     req = urllib2.Request(imgurl)
#     req.add_header('User-agent', headers())
#     html = urllib2.urlopen(req).read()
#     response =urllib2.urlopen(req)
#     f = open(name,'wb')
#     f.write(response.read())
#     f.close()
#     y=datetime.datetime.now()
#
#     print imgurl,(y-x).seconds

