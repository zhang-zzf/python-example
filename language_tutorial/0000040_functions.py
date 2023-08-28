#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import Any, Callable, Optional


def print_line(val: str, length=80):
    print(val.center(length, "*"))


# print_line(50, 100)

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
    """ concat

    :param args: arguments to concat
    :param sep:  the separator to join
    :return:  the joined str
    """
    return sep.join(args)


print(concat('a', 'b'))
print(concat('a', 'b', sep=','))

print_line('lambda')


def make_incrementor(n: int):
    """ Do nothing, but document it.

    No, really, it does not do anything.

    :param int n: the basement
    :return: the sum function
    """
    return lambda x: x + n


f1 = make_incrementor(5)
f11: Callable[[int], Callable[[Any], int | Any]] = make_incrementor
# 8
print(f1(3))

f2 = lambda x, y: x * y
# 10
print(f2(2, 5))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# key 需要一个函数
pairs.sort(key=lambda p: p[1])
print(pairs)

print_line("func args")


def func_args(arg1: int,  # arg1 是一个 int 类型（不包括 None)
              arg2: Optional[int],  # arg2 是 int|None 类型
              arg3: int = None,
              arg4: str = '',
              *args,  # args is a tuple
              **kwargs  # kwargs is a dict[str,any]
              ) -> None:
    print(f'arg1={arg1}, arg2={arg2}, arg3={arg3}, arg4={arg4}, args={args}, '
          + f'kwargs={kwargs}')


# key word args
# func_args() missing 1 required positional argument: 'arg2'
# 没有默认值的 args 都要传入参数
# func_args(arg1=1, a=1, b='2')
#
func_args(arg1=1, arg2=None, a=1, b='2')
func_args(arg1=1, arg2=None, arg3=None, a=1, b='2')
# linter 提示 Expected type 'int', got 'None' instead 。程序可以运行，可能会运行时报错
func_args(arg1=None, arg2=None, arg3=None, a=1, b='2')
#
# position args then key word args
# 位置参数需要根据参数位置依次填入参数，不能跳过
func_args(1, 2, 3, '4', 6, 7, 8, a=1, b="2")

print_line("多返回值")


def func_multi_return_values() -> (int, int, int):
    return 1, 2, 3


a, b, c = func_multi_return_values()
print(f'a={a}, b={b}, c={c}')

