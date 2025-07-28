#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict


def print_line(val: str, length=80):
    print(val.center(length, "*"))


# 0,1,2,3
for x in range(4):
    pass
# 1,2,3
for x in range(1, 4):
    pass
# 1,3
for x in range(1, 4, 2):
    print(x)

squares = [1, 4, 9, 16, 25]
for x in squares:
    val = x
for idx in range(len(squares)):
    val = (idx, squares[idx])
for idx, val in enumerate(squares):
    a_tuple = (idx, val)

users: dict[str, str] = {'Éléonore': 'inactive', 'Hans': 'active', '景太郎': 'active'}
for idx, key in enumerate(users):
    a_tuple = (idx, key)

# reverse
a_sum = 0
# 8,6,4,2,0
for x in reversed(range(0, 10, 2)):
    a_sum += x

# 排序
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for x in sorted(basket, reverse=True):
    val = x
# ['景太郎', 'Éléonore', 'Hans']
print(sorted(users, reverse=True))
# [('Hans', 'active'), ('Éléonore', 'inactive'), ('景太郎', 'active')]
print(sorted(users.items()))

# 去重 -> 排序
for x in sorted(set(basket)):
    val = x
