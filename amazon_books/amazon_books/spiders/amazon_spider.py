import scrapy


class AmazonSpider(scrapy.Spider):
    name = "Books"
    start_urls = ["https://www.amazon.in/si=stripbooks&ref=nb_sb_noss"]

    def parse(self, response):
        print(response.url)
