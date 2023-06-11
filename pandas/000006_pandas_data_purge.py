#!/usr/bin/env python
import sys

import pandas as pd


def print_line(val: str, length=80):
    print(val.center(length, "*"))


print_line("add na_values to pandas")
# pandas 把 na_values 中的值视为 NaN
na_values = ['na', '--']
data_frame = pd.read_csv("assets/property-data.csv", na_values=na_values)
print(data_frame.to_string())

print_line("check NaN")
num_bedrooms_series = data_frame["NUM_BEDROOMS"]
print(num_bedrooms_series)
# column1.isnull() 返回一个新的 Series
print(num_bedrooms_series.isnull())
print_line("fill NaN with 0")
# fillna 返回一个新的 Series
print(num_bedrooms_series.fillna(0))

# drop will check all the columns
print_line("drop NaN rows")
no_nan_df = data_frame.dropna()
print(no_nan_df)

# drop by column
print_line("dropna by ST_NUM")
print(data_frame.dropna(subset=["ST_NUM"]))

print_line("fill DataFrame with 0")
# fillin all the DataFrame
df_with_fill_0 = data_frame.fillna("0")
print(df_with_fill_0)

#
print_line("计算列")
st_num_series = data_frame["ST_NUM"]
# 均值， 中位数
print(st_num_series.mean(), st_num_series.median())
# 出现最多的行
print(st_num_series.mode())


def is_number(val: str) -> bool:
    try:
        float(val)
        return True
    except ValueError:
        return False


# 数据清洗
# watch out: float(NaN) = NaN
print_line("清洗数据")
df_copy = data_frame.copy(deep=True)
for row in df_copy.index:
    cell = df_copy.loc[row, 'NUM_BATH']
    if not is_number(cell):
        # df_copy.drop(row, inplace=True)
        df_copy.loc[row, 'NUM_BATH'] = 0
print(df_copy)
