import scrapy


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
        all_books = response.css("li.a-carousel-card")
        for book in all_books:
            book_title = book.css(
                ".acs-product-block__product-title").css("span.a-truncate-full::text").extract()
            book_author = book.css(
                "span.acs-product-block__contributor").css("span.a-truncate-full::text").extract()
            book_type = book.css(
                "span.acs-product-block__binding-value::text").extract()
            price = book.css("div.acs-product-block__price")
            current_price = price.css(
                "span.acs-product-block__price--buying").css("span.a-offscreen::text").extract()
            listed_price = price.css(
                "span.acs-product-block__price--strikethrough").css("span.a-offscreen::text").extract()
            book_rating = book.css("div.acs-product-block__rating")
            book_stars = book_rating.css("i").extract()
            book_review_count = book_rating.css(
                "span.acs-product-block__rating__review-count::text").extract()
            yield {
                'title': book_title,
                'author': book_author,
                'type': book_type,
                'current_price': current_price,
                'listed_price': listed_price,
                'rating': book_stars,
                'review_count': book_review_count
            }
