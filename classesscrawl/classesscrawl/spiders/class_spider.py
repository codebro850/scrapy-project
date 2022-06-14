from scrapy import Spider
from scrapy.selector import Selector
from classesscrawl.items import ClassesscrawlItem
class class_spider(Spider):
    name = "classes"
    allowed_domains = ["practice.geeksforgeeks.org"]
    start_urls = [
        "https://practice.geeksforgeeks.org/courses",
    ]
    def parse(self, response):
        classes = Selector(response).xpath('//div/a')

        for i in classes:
            item = ClassesscrawlItem()
            item['url'] = i.xpath('@href').extract()
            item['class_name'] = i.xpath('text()').extract()
            yield item
