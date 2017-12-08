from lxml import etree
import urllib2,urllib
from mmtaobao.cons import headers
from json import loads
import re

def openhtml(ht):
     req =urllib2.Request(ht)
     req.add_header('User-agent',headers())
     html = urllib2.urlopen(req).read()
     return html
if __name__ == "__main__":
    ht = "https://www.doutula.com"
    tt=openhtml(ht)
    print tt
    selector = etree.HTML(tt)
    print selector
    content = selector.xpath('//img[ends-with(@src,"jpg")]')
    x=0
    for each in content:
        urllib.urlretrieve(each, 'F:\learnPython\crawling\mmtaobao\pic\%s.jpg' % x)
        x+=1
        print "ok"