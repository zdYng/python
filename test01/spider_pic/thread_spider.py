#encoding: utf-8

import urllib
import threading
from bs4 import BeautifulSoup
import requests
import os
import time

FACE_URL_LIST = []

PAGE_URL_LIST = []

BASE_PAGE_URL = 'https://www.doutula.com/phone/list/?page='
for x in range(1,946):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

gLock = threading.Lock()

class Producer(threading.Thread):
    def run(self):
        while len(PAGE_URL_LIST)>0:
            gLock.acouire()
        else:
            face_url =FACE_URL_LIST.pop()
            gLock.release()
            filename = face_url.split('/')[-1]
            path = os.path.join('images',filename)
            urllib.urlretrieve(face_url,filename=path)

if __name__ == '__main__':
    for x in range(2):
        Producer().start()


