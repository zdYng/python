#coding:utf-8
import urllib2,re,urllib
from bs4 import BeautifulSoup

from mmtaobao.cons import headers

req = urllib2.Request('http://placekitten.com/')
req.add_header('user-agent',headers())
html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
urllib.urlretrieve(n,str(x)+'.jpg')
print 'OK....'



