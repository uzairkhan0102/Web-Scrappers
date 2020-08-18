import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.aljazeera.com']
    start_urls = ['https://www.aljazeera.com/news/']

    def parse(self, response):

        url = response.xpath("//a")

        for info in url:
            link = info.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_news, meta={'url': link})

    def parse_news(self, response):
        self.get_news(response)
        more_url = response.xpath("//a")

        for info in more_url:
            link = info.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.get_news, meta={'url': link})

    def get_news(self, response):
        url = response.request.meta['url']
        comp_url = 'https://www.aljazeera.com' + str(url)
        name = response.xpath("//h1[@class='post-title']/text()").get()
        tag = response.xpath("//li[@class='mini-secondary']/a/text()").get()
        author = response.xpath("//a[@rel='author']/text()").get()

        if not name:
            return

        yield {
            'url': comp_url,
            'name': name,
            'tag': tag,
            'author': author
        }
