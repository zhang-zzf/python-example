#!/usr/bin/env python

import pandas as pd
from pandas.core.indexing import _LocIndexer

from utils.printLine import print_line

myDataSet = {
    "Site": ["google", "runoob", "Wiki"],
    "Age": [10, 12, 13]
}
d1 = pd.DataFrame(myDataSet)
print(d1)

# with columns
print_line("with columns")
data = [["Google", 10.0], ["Runoob", 12], ['Wiki', 13]]
d2 = pd.DataFrame(data, columns=['Site', 'Age'])
print(d2)

# print row
print_line("print row")
d3 = pd.DataFrame({"calories": [420, 280, 390], "duration": [50, 45, 440]})
loc: _LocIndexer = d3.loc[[0]]
print(loc)
