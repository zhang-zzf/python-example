#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_line(val: str, length=80):
    print(val.center(length, "*"))


squares = [1, 4, 9, 16, 25]
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
