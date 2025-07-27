#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import sys

import fibo

print(f"path: {sys.path}")


def print_line(val: str, length=80):
    print(val.center(length, "*"))


print(f'[{os.path.basename(__file__)}] => {fibo.__name__}')
fib_to_5: list[int] = fibo.fib2(5)

if __name__ == "__main__":
    print_line("fib_to_5")
    print(fib_to_5)
