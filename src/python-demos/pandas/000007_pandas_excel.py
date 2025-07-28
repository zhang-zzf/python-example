#!/usr/bin/env python
import sys

import pandas as pd
from elasticsearch7 import Elasticsearch


def print_line(val: str, length=80):
    print(val.center(length, "*"))


excel = pd.read_excel("assets/支出2023-01-01～2023-06-03.xlsx", sheet_name=['2023-06-03'])
data_frame = excel['2023-06-03']
print(data_frame.to_string())

print_line("to json")

es = Elasticsearch(
    hosts="http://10.0.9.18:9200",
    http_auth=("elastic", "Gt4AvnA0zkqe")
)

# 去除单元格中的空格
data_frame.applymap(lambda val: str(val).strip())

for idx in data_frame.index:
    obj_json = data_frame.loc[idx].to_json(force_ascii=False)
    print(obj_json)
    resp = es.index(index="family_accounts_pay", body=obj_json)
    print(resp)
