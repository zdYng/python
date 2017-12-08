import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.crawler import CrawlerProcess

class MyImagePipe(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)


    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

if  __name__ =='__main__':
    process = CrawlerProcess({'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'})
    process.crawl(CnblogsSpider)
    process.start()

