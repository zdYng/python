# -*- coding:utf-8 -*-
from parsel import Selector
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#不写会报错

z = requests.get('https://www.qiushibaike.com/hot/')
z.status_code
z.text
sel =Selector(text=z.text)
t =sel.xpath('//div[@class="content"]/span/text()').extract()


for x in t:
    f = open(r'choushibaike.txt', 'a')
    f.write(x)
    f.close()