# -*- coding: utf-8 -*-
#!/usr/bin/env python
import urllib2,urllib
from bs4 import BeautifulSoup
import os
from mmtaobao.cons import headers
import random

class Scraper:
    def __init__(self,url):
        req =urllib2.Request(url)
        req.add_header('user-agent', headers())
        res = urllib2.urlopen(req)
        self.html = res.read()
        self.links =[]

    def parse(self,tag,attribute):
        soup =BeautifulSoup(self.html,'html.parser')
        tags =soup.find_all(tag)
        for link in tags:
            self.links.append(link.get(attribute))

    def download(self,directory):
        i = 0
        if not os.path.exists(directory):
            os.makedirs(directory)
        for link in self.links:
            i +=1
            #1
            #t=random.randint(1,100)
            #filename = directory+ 'photo' +str(i+t)+'.jpg'
            #file = open(filename,'w+')
            filename = directory + 'photo' + str(i) + '.gif'
            file = open(filename,'w+')
            urllib.urlretrieve(link,filename)
            print 'ok....'
            file.close()
        t= 'downloading is  end '
        return t

