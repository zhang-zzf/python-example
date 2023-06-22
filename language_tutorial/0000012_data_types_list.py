#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi


def print_line(val: str, length=80):
    print(val.center(length, "*"))


squares: list[int] = [1, 4, 9, 16, 25]
print_line("slice + slice")
a_slice_1 = squares + [36]
print(f'squares: {squares}')
print(f'a_slice_1: {a_slice_1}')
#
print_line('slice.append()')
# shadow copy
a_slice_2 = squares[:]
print(f'a_slice_2: {a_slice_2}')
a_slice_2.append(-1)
print(f'a_slice_2: {a_slice_2}')
#
print_line('slice.clear()')
a_slice_3 = squares[:]
print(f'a_slice_3 -> {a_slice_3}')
# clear [0,3)
a_slice_3[0:3] = []
print(f'a_slice_3 after clear [0:3] -> {a_slice_3}')
# clear all items
a_slice_3[:] = []
print(f'a_slice_3 after clear [:] -> {a_slice_3}')
#
print_line('slice for')
a_slice_4 = squares[:]
for x in a_slice_4:
    pass
a_map_4: dict[str, int] = {}
for idx in range(len(a_slice_4)):
    a_map_4[str(idx + 1)] = a_slice_4[idx]
print(f'a_map_4 -> {a_map_4}')
#
print_line("in slice")
# False
print(5 in squares)
# True
print(25 in squares)

#
# [1,    4,   9]
# first ...  last
print_line("append / extend at the last of the list")
a_slice_5 = squares[:]
a_slice_5.append(36)
a_slice_5.extend(range(1, 9, 3))
a_slice_5.extend([100, 200])
print(a_slice_5)

print_line('list.insert(i,x)')
a_slice_51 = squares[:]
# insert at the first of the list
a_slice_51.insert(0, 0)
# [0, 1, 4...]
print(a_slice_51)
# equal to a_slice_51.append(36)
a_slice_51.insert(len(a_slice_5), 36)
print(a_slice_51)

# list.pop() can be used to delete the first or the last item of the list
print_line('list.pop([i])')
a_slice_6 = squares[:]
# pop the last
# 25
print(a_slice_6.pop())
# 1
print(a_slice_6.pop(0))

print_line('列表推导式')
a_squares = list(map(lambda x: x ** 2, range(10)))
print(a_squares)
# 表达式 for if
# 表达式表示要对每个元素做的事情
# for 表示要操作的基础列表的范围
# if 表示对基础列表的过滤
a_squares_2 = [x ** 2 for x in range(10)]
a_squares_3 = [x ** 2 for x in range(10) if x % 2 != 0]
# [1, 9, 25, 49, 81]
print(a_squares_3)

pi_list = [str(round(pi, i)) for i in range(1, 6)]
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']
print(pi_list)
