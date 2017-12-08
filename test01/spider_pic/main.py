import requests
from bs4 import BeautifulSoup
import urllib
import os


PAGE_URL_LIST = []

BASE_PAGE_URL = 'https://www.doutula.com/article/list/?page='
for x in range(1,2):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

for page_url in PAGE_URL_LIST:

    response = requests.get(page_url)
    print response
    content =page_url.content

    soup = BeautifulSoup(content,'lxml')
    #print soup
    img_list =[]
    img_list = soup.find_all('img',attr={'class': 'lazy image_dtb img-responsive'})
    print len(img_list)
    print img_list
    for img in img_list:

        src = img['data-original']
        print src

        if not src.startswith('http'):
            src = 'http:' + src
            print src

        filename = src.split('/').pop()

        path =os.path.join('//images',filename)
        if urllib.urlretrieve(src,img+'.jpg')!=None:
            print("Processing")




