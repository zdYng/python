# coding:utf-8
from python27_spdier.baseSpider.DataOutput import DataOutput
from python27_spdier.baseSpider.HtmlDownloader import HtmlDownloader
from python27_spdier.baseSpider.HtmlParser import HtmlParser
from python27_spdier.baseSpider.URLManger import UrlManger

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManger()
        self.downloader = HtmlDownloader()
        self.parser =HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                #c从URL管理器获取新的URL
                new_url = self.manager.get_new_url()
                # HTML解析器抽取网页数据
                html = self.downloader.download(new_url)
                #将抽取的url添加到URL管理器中
                new_urls,data=self.parser.parser(new_url,html)
                #
                self.manager.add_new_urls(new_urls)
                #
                self.output.store_data(data)
                print "已经抓取%s个链接"%self.manager.old_url_size()
            except Exception,e:
                print "crawl failed"

        self.output.output_html()

if __name__ =="__main__":
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/286828.htm")


