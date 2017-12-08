#-*- coding:utf:8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import sys
import os
import time
import pymongo
# reload(sys)
# sys.setdefaulttencoding('utf-8')
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}


def get_detail_url():
    start_urls = ['http://www.ximalaya.com/dq/all/{}/'.format(pn) for pn in range(1,85)]#列表推导式，生产所有url
    print(start_urls)
    for start_url in start_urls:
        response = requests.get(start_url,headers=headers).text
        # print(response)
        soup = BeautifulSoup(response,'lxml')
        for item in soup.find_all('div',class_='albumfaceOutter'):
            # print(item)
            href = item.a['href']
            title = item.img['alt']
            img_url = item.img['src']
            content = {
                'href':href,
                'title':title,
                'img_url':img_url
            }
            cool.save(content)
            print('downloading {}...'.format(item.img['alt']))
            # print(item.a['href'])
            # break
            get_mp3(href,title)
            time.sleep(0.1)
            # break
        # break
def get_mp3(url,title):
    response = requests.get(url,headers=headers).text
    num_list = etree.HTML(response).xpath('//div[@class="personal_body"]/@sound_ids')[0].split(',')
    print(title+u'频道存在{}个音频'.format(len(num_list)))
    mkdir(title)
    os.chdir(r'home/xmly/'+title)#切换到指定目录下
    for id in num_list:
        json_url = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
        html = requests.get(json_url,headers=headers).json()
        # print(html)
        mp4_url = html.get('play_path')
        # print(mp4_url)
        download(mp4_url)
        print('{}下载成功'.format(mp4_url))

# 多进程，协程，并发
#切换目录 ———
def mkdir(title):
    '''
    对给定的title创建对应的文件夹
    :param title:
    :return:
    '''
    path = title.strip() #去空格
    isExist = os.path.exists(os.path.join(r'home/xmly/',path)) #拼接路径的作用，判断路径是否存在
    print(os.path.join(r'home/xmly/',path))
    if not isExist:
        print(u'创建{}'.format(title))
        os.makedirs(os.path.join(r'home/xmly/',title))
        return True
    else:
        print('{}文件夹存在!!!'.format(title))
        return False

def download(url):
    content = requests.get(url,headers=headers).content #为什么要用.content,返回2进制（图片，音频，视频）

    name = url.split('/')[-1]  #  wKgJnFoeY96DyiXSAG4JRJ7abr4415.m4a
    with open(name,'wb') as file:
        file.write(content)




if __name__ == '__main__':
        import threading
        def ddd():
            time.sleep(2)
            print(1111)
        th =threading.Thread(target=ddd())
        client = pymongo.MongoClient('localhost')
        db = client['xmly'] #连对应数据库
        cool = db['music'] #连对应表
        get_detail_url()

        #  多进程 ：
        #  协程 ： 在一个线程，遇到io切换 （和异步IO深入学习）
        # yied from

