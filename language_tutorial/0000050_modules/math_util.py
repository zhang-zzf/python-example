#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import fibo


def fib(n: int) -> list[int]:
    if n > 32:
        raise ValueError("n should be less than 32")
    ret: list[int] = []
    a, b = 0, 1
    for x in range(n):
        ret.append(b)
        a, b = b, a + b
    return ret


# 既可以把这个文件当脚本使用，也可以用作导入的模块，
# 因为，解析命令行的代码只有在模块以 “main” 文件执行时才会运行：
if __name__ == "__main__":
    print(f'Hello from {os.path.basename(__file__)}')
    print(f"cur module names: \n{dir()}")
    print(f"fibo module names: \n{dir(fibo)}")

