#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq

def print_line(val: str, length=80):
    print(val.center(length, "*"))


print_line('str methods -> len()')
# 5
a_str: str = "Hello"
print(len(a_str))
#
print_line('str methods -> encode()')
str_bytes: bytes = "Hello, 占占峰".encode(encoding='utf-8')
# b'Hello, \xe5\x8d\xa0\xe5\x8d\xa0\xe5\xb3\xb0'
print(str_bytes)
# Hello, 占占峰
print(str_bytes.decode(encoding='utf-8'))
