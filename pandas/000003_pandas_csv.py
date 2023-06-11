#!/usr/bin/env python
from typing import Optional

import pandas as pd
from pandas import DataFrame

from utils.printLine import print_line

print_line("read nba.csv")
data_frame: Optional[DataFrame] = pd.read_csv("assets/nba.csv")
print_line("info")
print(data_frame.info())
# 打印 all lines
# print(data_frame.to_string())
print_line("head 10")
print(data_frame.head(10).to_string())
print_line("tail 10")
print(data_frame.tail(10).to_string())
print_line("loc 1, 3, 5")
print(data_frame.loc[[1, 3, 5]].to_string())

print_line("write to site.csv")
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
data_frame = pd.DataFrame({'name': nme, 'site': st, 'age': ag})
# write to file
data_frame.to_csv("assets/sites.csv")
# format to csv string
print(data_frame.to_csv())
# format to json string
print_line("DataFrame to json")
print(data_frame.to_json())
