# -*- coding:utf-8 -*-
#协程
from gevent import monkey ; monkey.patch_all()
import sys
# reload(sys)
import requests
import gevent
from bs4 import BeautifulSoup
from lxml import etree
import os,time
from threading import Thread
from multiprocessing import Process


# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(),i)
#         gevent.sleep(0)
#
# g1 = gevent.spawn(f,5)
# g2 = gevent.spawn(f,5)
# g3 = gevent.spawn(f,5)
# g4 = gevent.spawn(f,5)
# g5 = gevent.spawn(f,5)
# g1.join()
# g2.join()
# g3.join()
# g4.join()
# g5.join()
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}

def fetch_url_text(url):
    response = requests.get(url, headers=headers).text
    return response

def get_url():
    try:
        start_urls = ['http://www.ximalaya.com/dq/book-%E6%82%AC%E7%96%91/{}/'.format(pn) for pn in range(1,85)]
        print(start_urls)
        urls_list = []
        for start_url in start_urls:
            urls_list.append(start_url)
            # response = fetch_url_text(start_url)
            # soup  = BeautifulSoup(response,'lxml')
            # print(soup)
            # break
            # for item in soup.find_all('div',class_='albumfaceOutter'):
            #     print(item)
            #     href = item.a['href']
            #     title = item.img['alt']
            #     img_url = item.img['src']
            #     # print(title)
            #     content = {
            #         'href':href,
            #         'title':title,
            #         'img_url':img_url
            #     }
            #     get_mp3(href,title)
        #协程模块1
        jobs = [gevent.spawn(fetch_url_text,url) for url in urls_list]
        gevent.joinall(jobs)
        [job.value for job in jobs]
        for response in  [job.value for job in jobs]:
            soup = BeautifulSoup(response,'lxml')
            for item in soup.find_all('div',class_='albumfaceOutter'):
                print(item)
                href = item.a['href']
                title = item.img['alt']
                img_url = item.img['src']
                # print(title)
                content = {
                    'href':href,
                    'title':title,
                    'img_url':img_url
                }
                get_mp3(href,title)
    except Exception as e:
       print(e)
    return ''

def fetch_json(id):
    json_url = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
    html = requests.get(json_url, headers=headers).json()
    return html

def get_mp3(url,title):
    response = fetch_url_text(url)
    num_list = etree.HTML(response).xpath('//div[@class="personal_body"]/@sound_ids')[0].split(',')
    print(num_list)

    mkdir(title)
    os.chdir(r'F:\xmly\\'+title)
    ii=1
    list_ids = []
    for id in num_list:
        list_ids.append(id)
        # print(id)
        # # json_url = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
        # html = fetch_json(id)
        # # print(html)
        # mp3_url = html.get('play_path')
        # # print(mp3_url)
        # # download(mp3_url)
        # content = requests.get(mp3_url, headers=headers).content
        # name = title + '_%i.m4a'%ii
        # with open(name, 'wb') as file:
        #     file.write(content)
        # print("{} download is ok".format(mp3_url))
        # ii+=1
    #协程模块2
    jobs = [gevent.spawn(fetch_json,id) for id in list_ids]
    gevent.joinall(jobs)
    [job.value for job in jobs]
    for html in [job.value for job in jobs]:
        mp3_url = html.get('play_path')
        content = requests.get(mp3_url, headers=headers).content
        name = title + '_%i.m4a' % ii
        with open(name, 'wb') as file:
            file.write(content)
        print("{} download is ok".format(mp3_url))
        ii += 1

        # break
# def download(url):
#     content = requests.get(url,headers=headers).content
#     name = url.split('/')[-1]
#     with open(name,'wb') as file:
#         file.write(content)

def mkdir(title):
    path = title.strip()
    isExist = os.path.exists(os.path.join(r'F:\xmly\\',path))
    if not isExist:
        os.makedirs(os.path.join(r'F:\xmly\\',title))
        print("{} file is created".format(title))
        return True
    else:
        print("Existed {} file".format(title))
        return False


if __name__ == "__main__":
    get_url()