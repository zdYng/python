# -*- coding: utf-8 -*-
#!/usr/bin/env python
import urllib2,urllib
from mmtaobao.cons import headers
from json import loads
import re

html = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B8%E3%D0%A6%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&'
req =urllib2.Request(html)
req.add_header('user-agent',headers())
html_open = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
print html_open
