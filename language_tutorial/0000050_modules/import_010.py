#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path

import fibo


def print_line(val: str, length=80):
    print(val.center(length, "*"))


print(f'[{os.path.basename(__file__)}] => {fibo.__name__}')
fib_to_5: list[int] = fibo.fib2(5)
