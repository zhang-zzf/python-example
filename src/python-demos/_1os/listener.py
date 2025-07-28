import time

from _1os.get_wan_ip6 import WanIP6


class Listener:
    ipv6 = ''

    @staticmethod
    def notify():
        print(Listener.ipv6)

    def start(self):
        ip_getter = WanIP6()
        while True:
            ipv6 = ip_getter.get_wan_ip6()
            if ipv6 != Listener.ipv6:
                Listener.ipv6 = ipv6
                self.notify()
            time.sleep(16)


class Notifier:
    def notify(self):
        pass


class DingDingNotifier(Notifier):
    def notify(self):
        pass


if __name__ == '__main__':
    Listener().start()
