# 伪装 UA user-agent
from http.client import HTTPResponse
from urllib import request
from urllib.request import Request

url: str = "http://httpbin.org/get"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36'
}
req: Request = request.Request(url, headers=headers)

# go get the data
resp: HTTPResponse = request.urlopen(req)
json: str = resp.read().decode("utf-8")
print(json)
