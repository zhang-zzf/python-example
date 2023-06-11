#!/usr/bin/env python

import pandas as pd


def print_line(val: str, length=80):
    print(val.center(length, "*"))


print_line("read json")
data_frame = pd.read_json("assets/sites.json")
print(data_frame.to_string())
