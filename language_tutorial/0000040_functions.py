#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict, List, Any


def print_line(val: str, length=80):
    print(val.center(length, "*"))


def fib(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


def fib2(n: int) -> list[int]:
    ret: list[int] = []
    a, b = 0, 1
    while a < n:
        ret.append(a)
        a, b = b, a + b
    return ret


print(fib(1), fib(2), fib(3), fib(4))
print(fib2(100))

print_line("Default Argument Values")


def ask_ok(ok: str, retries=4, reminder="Please try again!") -> bool:
    while True:
        if ok in ('y', "Y", 'yes', "Yes",):
            return True
        if ok in ('n', "N", 'no', 'No',):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user input')
        print(reminder)


if ask_ok("y"):
    print("Yes")
# position args
ask_ok('no', 2, "try Again!")

print_line('Keyword Arguments')
# 无视 param 位置
# keyword args
ask_ok('Yes', reminder="Sorry, Try Again!")
ask_ok("No", reminder="?", retries=2)


def a_func(arg1: int, *args, **kwargs):
    print('-- arg1: ', arg1)
    for arg in args:
        print(arg)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])


a_func(arg1=0)
# position args then keyword args
a_func(0, 'a', 1, 2, 3, a="b", c="d")
a_func(arg1=0, a="b", c="d")

print_line('Arbitrary Argument Lists')


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep='/') -> str:
    return sep.join(args)


print(concat('a', 'b'))
print(concat('a', 'b', sep=','))
