# coding:utf-8
from TestUnit.SpiderDataOutput import SpiderDataOutput
from TestUnit.SpiderDownloader import SpiderDownloader
from TestUnit.SpiderParser import SpiderParser

class SpiderMan(object):

    def __init__(self):
        self.downloader =SpiderDownloader()
        self.parser = SpiderParser()
        self.output =SpiderDataOutput()

    def crawl(self,root_url):

        content =self.downloader.download(root_url)

        for info in  self.parser.get_kw_cat(content):
            print info
            cat_name =info['cat_name']
            detail_url = 'http://ts.kuwo.cn/service/getlist.v31.php?act=detail&id=%s'%info['id']
            content = self.downloader.download(detail_url)
            details = self.parser.get_kw_detail(content)
            print detail_url
            self.output.output_html(self.output.filepath,details)
        self.output.output_end(self.output.filepath)

if __name__ == "__main__":
    html ='http://ts.kuwo.cn/service/getlist.v31.php?act=cat&id=50'
    spider =SpiderMan()
    spider.crawl(html)