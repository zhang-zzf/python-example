# fake_useragent

from fake_useragent import UserAgent

ua: UserAgent = UserAgent()

# 特殊用法，通过 fake_useragent.fake.FakeUserAgent.__getattr__ 获取属性
print(ua.ie)
print(ua.msie)
print(ua["internet explorer"])
print(ua.edge)
# google chrome
print(ua.google)
print(ua.chrome)
print(ua.chrome)
# firefox
print(ua.ff)
print(ua.firefox)
# safari
print(ua.safari)
# opera
print(ua.opera)
