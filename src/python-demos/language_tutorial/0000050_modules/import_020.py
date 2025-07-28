#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fibo import fib2


def print_line(val: str, length=80):
    print(val.center(length, "*"))


fib_to_5: list[int] = fib2(5)
