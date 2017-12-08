# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request
import os
import re
import imp,sys
import importlib
importlib.reload(sys)




for i in range(1,10):
   html = request.urlopen('http://desk.zol.com.cn/chuangyi/%s.html' %i)
   html=html.read()
#print html
   soup = BeautifulSoup(html,'html.parser',from_encoding='gbk')

   lis = soup.find_all('li',class_="photo-list-padding")

   info_list = []

   for li in lis:
      temp={}
      a = li.find_all('a')[0]
      img = li.find_all('img')[0]
    # print img
      temp['url'] = "http://desk.zol.com.cn%s" %a['href']
      temp['title'] = img['alt']
    # print temp['title']
      info_list.append(temp)

# print len(info_list)
#print info_list
   for info in info_list:

      # print(info['url'])
      respons1 = request.urlopen(info['url'])
      response1 = respons1.read()
      soup1 = BeautifulSoup(response1,'html.parser',from_encoding='gbk')
      ul = soup1.find_all('ul',id="showImg")[0]
      img_lis = ul.find_all('li')


      bigimg_list =[]
      for li in img_lis:
         img = li.find_all('img')[0]

         # print img
         try:
             ur = img['src']
             u = re.compile('144x90')
             url = u.sub('1600x900',ur)
             print(url)
         except Exception as e:
             ur = img['srcs']
             u = re.compile('144x90')
             url = u.sub('1600x900', ur)
             print(url)

         bigimg_list.append(url)
      # print(bigimg_list)

      t=info['title']
      j = 1
      os.makedirs(info['title'])

      for url in bigimg_list:
        img_dat = request.urlopen(url)
        img_data = img_dat.read()
        try:
          with open('%s\\%s.jpg'%(t,j),'wb') as f:
            f.write(img_data)
            j +=1
        except Exception as e:
            pass

            #f.close()


