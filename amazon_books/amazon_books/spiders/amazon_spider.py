import scrapy
from ..items import AmazonBooksItem


class AmazonSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://www.amazon.in/s?k=books"]

    def parse(self, response):
        item = AmazonBooksItem()
        all_books = response.css("div.s-main-slot").css("div.s-asin")
        for book in all_books:
            book_title = book.css(
                "h2.s-line-clamp-2").css("span.a-color-base::text").extract()[0]
            if not book_title:
                continue
            book_author = book.css(
                "div.a-row").css("a.a-link-normal::text").extract()[0]
            product_details = book.css("div.a-spacing-top-small")
            book_binding = product_details.css(
                "a.a-text-bold::text").extract()[0]
            prices = product_details.css(
                "span.a-price").css("span.a-offscreen::text").extract()
            current_price = prices[0]
            if prices[1]:
                listed_price = prices[1]
            book_rating = book.css("div.a-spacing-top-micro")
            book_stars = book_rating.css("i")[0].xpath(
                "@class").extract()[0]
            book_review_count = book_rating.css(
                "span.a-size-base::text").extract()[0]

            item['title'] = book_title
            item['author'] = ' '.join(book_author.split())
            item['binding'] = ' '.join(book_binding.split())
            item['current_price'] = current_price
            item['listed_price'] = listed_price
            item['rating'] = book_stars.split()[2][13:].replace('-', '.')
            item['review_count'] = book_review_count
            yield item
