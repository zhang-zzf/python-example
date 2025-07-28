import http.client
import urllib.request
import urllib.response

resp: http.client.HTTPResponse = urllib.request.urlopen("http://www.baidu.com")

html: str = resp.read().decode("utf-8")
print(html)
