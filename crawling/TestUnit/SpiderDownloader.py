# coding: utf-8
import requests
class SpiderDownloader(object):
    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        headers={'User-Agent':user_agent}
        r = requests.get(url,headers=headers)

        if r.status_code==200:
            r.encoding='utf-8'
            t=r.content
            return t