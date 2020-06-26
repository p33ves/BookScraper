import scrapy


class AmazonSpider(scrapy.Spider):
    name = "Books"
    start_urls = ["https://www.amazon.in/s?i=stripbooks&ref=nb_sb_noss"]

    def parse(self, response):
        # print(response.url)
        page_title = response.css("title::text").extract_first()
        yield {"page_title": page_title}
        book_details = response.css("span.a-truncate-full::text").extract()
        current_whole_prices = response.css(
            "span.a-price-whole::text").extract()
        all_prices = response.css("span.a-offscreen::text").extract()
