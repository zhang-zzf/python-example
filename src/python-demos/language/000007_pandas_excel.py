#!/usr/bin/env python
import sys

import pandas as pd


def print_line(val: str, length=80):
    print(val.center(length, "*"))


ojb1 = {
    "a": 1,
    "b": "2",
    "c": [1, 2],
    "d": {
        "da": [1, 2, 3]
    }
}
