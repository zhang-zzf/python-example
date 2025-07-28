from http.client import HTTPResponse
from urllib import parse, request
from urllib.request import Request

from fake_useragent import UserAgent


def search_baidu():
    utf_8 = 'utf-8'
    word = input('请输入搜索关键字: ')
    # send the http request
    url = 'https://www.baidu.com/s?wd={}'.format(parse.quote(word))
    headers = {
        'User-Agent': UserAgent().chrome
    }
    resp: HTTPResponse = request.urlopen(Request(url, headers=headers))
    html = resp.read().decode(utf_8)
    # save the response
    filename = word + '.html'
    with open(filename, "w", encoding=utf_8) as file:
        file.write(html)


if __name__ == '__main__':
    search_baidu()
