from urllib import request
from http.client import HTTPResponse


class WanIP6:

    def get_wan_ip6(self):
        """
        查询本机ip6地址
        :return: ip
        """
        resp: HTTPResponse = request.urlopen('https://6.ipw.cn')
        ipv6 = resp.read().decode('utf-8')
        return ipv6


if __name__ == '__main__':
    print(WanIP6().get_wan_ip6())
