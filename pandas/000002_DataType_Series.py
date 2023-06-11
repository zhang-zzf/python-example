#!/usr/bin/env python

import pandas as pd

# series with default index (starts from 0)
s1 = pd.Series([1, 2, 3])
print(s1)
# series with custom index
s2 = pd.Series(["a", "b", "c"], index=["1", "2", "3"])
print(s2)
print(s2["2"])

# build series from map
s3 = pd.Series({"a": "zhang", "b": "5", 6: 6})
print(s3)
print(s3[6])
