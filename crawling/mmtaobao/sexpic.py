# -*- coding: utf-8 -*-
import requests
import urllib2,re
import os
from mmtaobao.cons import headers
from lxml import etree
from parsel import Selector

import datetime
html =requests.get("http://cl.j4q.pw/htm_data/2/1709/2664044.html")

html.encoding = 'utf-8'
# req = urllib2.Request('http://cl.j4q.pw/htm_data/2/1709/2664044.html')
# req.add_header('user-agent', headers())
# html = urllib2.urlopen(req).read()
print html.content
# select = Selector(html.text)
# content =select.xpath('//div//img/@src')
regt = r'<img src="(.*?)" onclick="(?#...)" style="cursor:pointer>"'
hh = re.findall(regt, html)
print hh

# for imgurl in content:
#
#     x=datetime.datetime.now()
#
#     name = imgurl[-7:-1]
#     os.chdir(r"D://pic")
#     req = urllib2.Request(imgurl)
#     req.add_header('User-agent', headers())
#     #html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
#     response =urllib2.urlopen(req)
#     f = open(name,'wb')
#     f.write(response.read())
#     f.close()
#     y=datetime.datetime.now()
#
#     print imgurl,(y-x).seconds

