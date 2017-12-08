# -*- coding: utf-8 -*-
#!/usr/bin/env python


import urllib2
from mmtaobao.cons import headers
mmurl = 'https://mm.taobao.com/json/request_top_list.htm?type=0&page='
i = 0
ph =-1
temp ='''<img src='''
while i<4:
    url = mmurl + str(i)
    print url
    up = urllib2.urlopen(url)
    cont=up.read().decode('gbk').encode('utf-8')
    # head="<img src"
    # tail=".jpg"
    # ph = cont.find(head)
    # pj = cont.find(tail,ph+1)
    # print cont[ph+len(temp)+1:pj+len(tail)]
    # print '--------------------------------'
    # print cont
    # print '--------------------------------'
    ahref ="<a href"
    target ="target"
    pa = cont.find(ahref)
    pt = cont.find(target,pa)
    #print cont[pa + len(ahref)+4 : pt - 2]
    modelurl=cont[pa + len(ahref)+4 : pt - 2]
    ht = 'https://'+modelurl
    print ht
    mup =urllib2.urlopen(ht)
    mcont = mup.read().decode('gbk').encode('utf-8')
    #print mcont
    imgh ="<img style"
    imge =".jpg>"
    iph = mcont.find(imgh)
    ipe =mcont.find(imge,iph)
    print mcont[iph:ipe]

    i +=1