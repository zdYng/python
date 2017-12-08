# coding:utf-8
import scrapy
import selector
from items import CnblogspiderItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.crawler import CrawlerProcess
from scrapy import Request
from scrapy import Selector


class CnblogsSpider(scrapy.Spider):

    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/qiyeboy/default.html?page=1"]
    def parse(self, response):
        papers =response.xpath(".//*[@class='day']")

        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title=paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            item = CnblogspiderItem(url=url,title=title,time=time,content=content)
            request = scrapy.Request(url=url,callback=self.parse_body)
            request.meta['item'] = item
            yield request

            # print url,title,time,content
        #翻页
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0],callback=self.parse)
    def parse_body(self,response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['cimage_urls'] = body.xpath('.//img//@src').extract()
        yield item


class MyImagePipe(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item


if __name__ == '__main__':
    process = CrawlerProcess({'USER_AGENT':
                             'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'})
    process.crawl(CnblogsSpider)
    process.start()