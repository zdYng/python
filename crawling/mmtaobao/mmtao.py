# -*- coding: utf-8 -*-
#!/usr/bin/env python
import urllib2,urllib
from mmtaobao.cons import headers
from json import loads
import re

def getUrlList():
    req =urllib2.Request('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
    req.add_header('user-agent',headers())

    html = urllib2.urlopen(req,
                data='q&viewFlag=A&sortType=default&sea'
                     'rchStyle=&searchRegion=city%3'
                     'A&searchFansNum=&cur'
                     'rentPage=1&pageSize=100').read().decode('gbk').encode('utf-8')
    json = loads(html)
    return json['data']['searchDOList']

def getInfo(userId):
    req =urllib2.Request('https://mm.taobao.com/self/aiShow.htm?userId=%s'%userId)
    req.add_header('User-agent',headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    #print html

def getAlbumList(userId):
    req = urllib2.Request('https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%%20=%s' % userId)
    req.add_header('user-agent', headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    #print html
    reg = r'class="mm-first" href="//(.*?)"'
    n =re.findall(reg,html)[::2]
    return n

def pichtml(n):

    req = urllib2.Request(n)
    req.add_header('user-agent', headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')

    reg = r'class="mm-template-src" src="(.+?\.jpg)"'

    imglist = re.findall(reg,html)
    print imglist
    x = 0
   # for imgurl in imglist:
        #print imgurl
       # urllib.urlretrieve(imgurl,'F:\\learnPython\\crawling\\mmtaobao\\pic\\%s.jpg' %x)
     #   x= x+1






for i in  getUrlList():
    userId=i['userId']
    #getInfo(userId)
    for n in getAlbumList(userId):
        print n
         #pichtml(n)






