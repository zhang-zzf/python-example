import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote_div in response.xpath('//div[@class="quote"]'):
            print('text', quote_div.xpath('./span[@class="text"]/text()').get())
            print('author', quote_div.xpath('//small/text()').get())
            print('tags', quote_div.xpath('//a[contains(@href, "tag")]/text()').getall())
            yield {
                'text': quote_div.xpath('./span[@class="text"]/text()').get(),
                'author': quote_div.xpath('//small/text()').get(),
                'tags': quote_div.xpath('//a[contains(@href, "tag")]/text()').getall()
            }
