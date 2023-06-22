#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_line(val: str, length=80):
    print(val.center(length, "*"))


# 创建空集合只能用 set()，不能用 {}，{} 创建的是空字典
a_set_1 = set()
# a_set_2 = set([1, 2])
a_set_2 = {1, 2}
# set will remove the duplicates
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# {'banana', 'orange', 'apple', 'pear'}
# 注意 set 是无序
print(basket)

# set 也可以使用推导式
a_set_3 = {x for x in 'abracadabra' if x not in 'abc'}
