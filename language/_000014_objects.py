#!/usr/bin/env python

import re
from typing import Optional, Match, Union, Any

# 查询分页
val: str = 'https://vip.91p321.com/v.php?category=rf&viewtype=basic&page=12'
pattern = re.compile(r'page=(\d+)')
search: Optional[Match[str]] = pattern.search(val)
pageNo = int(search.group(1))
print(search, pageNo)
