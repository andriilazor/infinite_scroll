import scrapy


class ArticlesSpider(scrapy.Spider):
    name = "articles"
    start_urls = ["https://infiniteajaxscroll.com/examples/articles/"]

    def parse(self, response):
        for article in response.css("div.article"):
            yield {
                "title": article.css("h1::text").get(),
                "text": " ".join(article.css("p::text").getall()),
                "images": article.css("img::attr(src)").getall(),
            }
        yield from response.follow_all(css="a.pager__next", callback=self.parse)
