#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Fibonacci numbers module
import os


def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n) -> list[int]:  # return Fibonacci series up to n
    """ fibonacci

    :param n: the last one
    :return: list[int]
    """
    result: list[int] = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# python fibo.py 等同于 ./fibo.py
# ./fibo.py -> '__main__'
print(f'[{__file__}] => {__name__}')
# 既可以把这个文件当脚本使用，也可以用作导入的模块，
# 因为，解析命令行的代码只有在模块以 “main” 文件执行时才会运行：
if __name__ == "__main__":
    print("Hello from fibo.py")
