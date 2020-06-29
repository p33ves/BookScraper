import scrapy
from ..items import AmazonBooksItem


class AmazonSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://www.amazon.in/s?i=stripbooks&ref=nb_sb_noss"]

    def parse(self, response):
        """ print(response.url)
        page_title_css = response.css("title::text").extract_first()
        page_title_xpath = response.xpath("//title/text()").extract()
        yield {"page_title": [page_title_css, page_title_xpath]}
        book_details_css = response.css("span.a-truncate-full::text").extract()
        book_details_xpath = response.xpath(
            "//span[@class='a-truncate-cut']/text()").extract()
        current_whole_prices = response.css(
            "span.a-price-whole::text").extract()
        all_prices = response.css("span.a-offscreen::text").extract()
        """
        item = AmazonBooksItem()
        all_books = response.css("li.a-carousel-card")
        for book in all_books:
            book_title = book.css(
                ".acs-product-block__product-title").css("span.a-truncate-full::text").extract()[0]
            book_author = book.css(
                "span.acs-product-block__contributor").css("span.a-truncate-full::text").extract()[0]
            book_binding = book.css(
                "span.acs-product-block__binding-value::text").extract()[0]
            price = book.css("div.acs-product-block__price")
            current_price = price.css(
                "span.acs-product-block__price--buying").css("span.a-offscreen::text").extract()[0]
            listed_price = price.css(
                "span.acs-product-block__price--strikethrough").css("span.a-offscreen::text").extract()[0]
            book_rating = book.css("div.acs-product-block__rating")
            book_stars = book_rating.css("i")[0].xpath(
                "@class").extract()[0]
            book_review_count = book_rating.css(
                "span.acs-product-block__rating__review-count::text").extract()[0]

            item['title'] = book_title
            item['author'] = ' '.join(book_author.split())
            item['binding'] = book_binding
            item['current_price'] = current_price
            item['listed_price'] = listed_price
            item['rating'] = book_stars.split()[2][14:].replace('-', '.')
            item['review_count'] = book_review_count[1:-1]
            yield item
