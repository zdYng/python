# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request
from mmtaobao.cons import headers
import os
import re
import urllib2,urllib

def url_open(url):
    req = urllib2.Request(url)
    req.add_header('user-agent',headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    return html

def get_soup(html,a,b):
    soup = BeautifulSoup(html,'html.parser',from_encoding='gbk')
    lis = soup.find_all(a,class_=b)
    return lis
