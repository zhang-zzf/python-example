import json

import scrapy
from scrapy.http import Response


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    start_urls = [
        'http://httpbin.org/anything'
    ]

    custom_settings = {
        'USER_AGENT': 'zzf.zhang',
    }

    def parse(self, response):
        print(response)
        json_obj = json.loads(response.body)
        print(json_obj)


class HttpbinSpider2(scrapy.Spider):
    name = "httpbin2"
    start_urls = [
        'http://httpbin.org/anything'
    ]

    custom_settings = {
        'USER_AGENT': 'zzf.zhang',
    }

    def parse(self, response):
        print(response)
        json_obj = json.loads(response.body)
        print(json_obj)


class HttpBaiduCom(scrapy.Spider):
    name = "baidu"
    start_urls = [
        'https://www.baidu.com'
    ]

    custom_settings = {
        'USER_AGENT': 'zzf.zhang',
    }

    def parse(self, response: Response):
        print(response)
        print(response.text)
