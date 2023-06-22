#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
