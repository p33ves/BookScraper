import scrapy


class AmazonSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://www.amazon.in/s?i=stripbooks&ref=nb_sb_noss"]

    def parse(self, response):
        # print(response.url)
        page_title_css = response.css("title::text").extract_first()
        page_title_xpath = response.xpath("//title/text()").extract()
        yield {"page_title": [page_title_css, page_title_xpath]}
        book_details_css = response.css("span.a-truncate-full::text").extract()
        book_details_xpath = response.xpath(
            "//span[@class='a-truncate-cut']/text()").extract()
        current_whole_prices = response.css(
            "span.a-price-whole::text").extract()
        all_prices = response.css("span.a-offscreen::text").extract()
