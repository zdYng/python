# -*- coding: utf-8 -*-
#!/usr/bin/env python
from mmtaobao.scraper import Scraper





#1
for i in range(2,23):
    html = 'http://www.mm131.com/xinggan/2229_%s.html' % i
    scraper =Scraper(html)
    scraper.parse('img','src')

    scraper.download('pic\\')

#2
# scraper =Scraper('https://www.doutula.com/')
# scraper.parse('img','src')
# scraper.download('pic//')
print 'all  .....end'