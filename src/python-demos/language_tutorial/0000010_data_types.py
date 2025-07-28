#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_line(val: str, length=80):
    print(val.center(length, "*"))


print_line('data type: int/float')
a_int = 3
print('1 in binary 3 => ', a_int.bit_count())
print(int(5.6), int(float('5.6')))
#
print_line('data type: str')
aStr1 = "Hello"
aStr2: str = 'World'
# 第一行和最后一行都有一个换行符
aStr3: str = '''
select * 
from users
where id = 1
'''
print(aStr1, aStr2, aStr3)
print_line('data type: str')
# 保留所有格式
# 第一行没有换行符
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print_line('data type: raw str')
# C:\some
# ame
print('C:\some\name')
# r'' 不会把前置 \ 的字符转义成特殊字符
# C:\some\name
print(r'C:\some\name')

#
print_line("bool")
a_true: bool = True
a_false: bool = False
a_bool = True
# False, True
print(bool(0), bool(1))
# False, True
print(bool(''), bool(' '))

# str to num
# num to str
print_line("str <-> num")
print(str(430043), int('43'))

# None == None ?
print_line("None == None")
print(None == None)

# in 判断集合中是否存在元素
print_line("in to check if a item is in a collection")
a_list = [1]
a_set = {1}
a_map = {"a": 1}
print(f'{1 in a_list}, {1 in a_set}, {"a" in a_map}, {1 in a_map}')
