#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys as system


def print_line(val: str, length=80):
    print(val.center(length, "*"))


# 0. 内置 module
print(system.builtin_module_names)

# 1. sys.path
# 输入脚本的目录（或未指定文件时的当前目录）。
#
# PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）。
#
# 依赖于安装的默认值（按照惯例包括一个 site-packages 目录，由 site 模块处理）。
print(system.path)

# list 当前模块中定义的名称
print(dir())
