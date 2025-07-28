import re

import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse


class Top250Spider(scrapy.Spider):
    name = "Top250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    # 被 douban block， 限制下载速度
    custom_settings = {
        # 10 second
        'DOWNLOAD_DELAY': 16,
        # 16 * [0.5, 1.5]
        'AUTOTHROTTLE_ENABLED': True,
        # 对单个网站进行并发请求的最大值，默认为8
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        # Configure maximum concurrent requests performed by Scrapy (default: 16)
        'CONCURRENT_REQUESTS': 16,
        # 当前目录
        'IMAGES_STORE': '/tmp'
    }

    # 登陆后使用 cookie
    cookies = {}

    @classmethod
    def import_cookies(cls, cookie_str: str):
        for c in cookie_str.split(';'):
            item = c.split('=', 1)
            cls.cookies[item[0].strip()] = item[1].strip()

    def start_requests(self):
        return [Request(url, cookies=self.cookies, dont_filter=True, callback=self.parse_list_page)
                for url in self.start_urls]

    def parse_list_page(self, response: HtmlResponse, **kwargs):
        # extract link to detail page
        for a_tag in response.css(".hd a"):
            yield Request(a_tag.attrib["href"], cookies=self.cookies, callback=self.parse_detail_page)
        # extract link to next page
        for next_page in response.css(".next a"):
            yield Request(response.urljoin(next_page.attrib["href"]), cookies=self.cookies, callback=self.parse_list_page)

    def parse_detail_page(self, response: HtmlResponse, **kwargs) -> dict[str, object]:
        info_div = response.css("#info").get()
        intro = response.css('#link-report-intra .all').css('span::text').get()
        if intro is None:
            intro = response.css('#link-report-intra span::text').extract_first()
        poster_img = response.css('#mainpic img::attr(src)').get()
        return {
            # 片名 response.css("#content h1 span::text").getall()
            "name": " ".join(response.css("#content h1 span::text").getall()),
            # 语言 response.css("#info span.pl").getall() 选不到语言的值
            "language": re.search(r'<span class="pl">语言:</span> (.*)<br>', info_div).group(1),
            # div#info 块使用了非结构化的 html，使用 regex 来抽取需要的数据
            "imdb_id": re.search(r'<span class="pl">IMDb:</span> (.*)<br>', info_div).group(1),
            "rating_num": float(response.css(".rating_num").css('strong::text').get()),
            'desc': intro.strip('\n').strip(),
            # 海报 url
            'poster_img': poster_img,
            # 海报本地存储相对路径
            'poster_img_path': None,
            # 海报 url 放入 item.image_urls 中，ImagesPipeline 会自动下载其中的图片
            "image_urls": [poster_img]
        }
