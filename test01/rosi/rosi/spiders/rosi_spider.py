import scrapy
class RosiSpider(scrapy.spiders.Spider):
    name = "rosi"
    allowed_domains = ["doutula.com"]
    start_urls = ["http://www.doutula.com"]

    def parse_url(self,response):
        print response.url
if __name__ =='__main__':
    s =RosiSpider()
    s.parse_url()