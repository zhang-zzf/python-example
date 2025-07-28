#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从包中导入 包 / 模块 / 模块内名称
# 导入整包 package
import urllib3
# 导入 urillib3 的子包
import urllib3.util
# 导入 exceptions 模块
import urllib3.exceptions

# 导入 子包
from urllib3 import packages
# 导入模块
from urllib3.util import timeout
from urllib3 import request
# 导入模块内的名称
from urllib3.util.timeout import Timeout
from urllib3.request import RequestMethods


def print_line(val: str, length=80):
    print(val.center(length, "*"))


a_class = urllib3.HTTPResponse
a_func = urllib3.proxy_from_url

http_error = urllib3.exceptions.HTTPError()

time = urllib3.util.current_time

methods = request.RequestMethods

print(f"cur module names: \n{dir()}")
print(f"urllib3 module names: \n{dir(urllib3)}")
