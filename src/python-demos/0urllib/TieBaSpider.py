import random
import time
from http.client import HTTPResponse
from urllib import request, parse
from urllib.request import Request

from fake_useragent import UserAgent


class TieBaSpider:

    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?'
        self.params = None
        self.headers = {
            'User-Agent': UserAgent().chrome
        }
        self.html_charset = 'utf-8'
        self.html = None

    def reset_req(self, params: dict[str, object]):
        self.params = params
        self.url = self.url + parse.urlencode(params)
        return self

    def get_html(self):
        req: Request = Request(self.url, headers=self.headers)
        resp: HTTPResponse = request.urlopen(req)
        self.html = resp.read().decode(self.html_charset)
        return self

    def parse_html(self):
        return self

    def write_html(self):
        filename: str = self.params['kw'] + str(self.params['page']) + '.html'
        with open(filename, 'w') as file:
            file.write(self.html)
        return self

    def run(self):
        req_params: dict[str, object] = {
            'kw': input("Please input the search key work: "),
            'page': 0,
            'pn': 0
        }
        pages: int = int(input('Please input the pages[3]: '))
        for page in range(1, pages + 1):
            req_params['page'] = page
            req_params['pn'] = (page - 1) * 50
            self.reset_req(req_params)
            self.get_html().parse_html().write_html()
            # sleep some time: [1,8] seconds
            time.sleep(random.randint(1, 8))


if __name__ == '__main__':
    spider = TieBaSpider()
    spider.run()
