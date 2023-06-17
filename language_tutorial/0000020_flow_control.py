#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict


def print_line(val: str, length=80):
    print(val.center(length, "*"))


def if_func(x: int):
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')


# switch
# 遇到第一个 case 返回
def match_func(status: int) -> str:
    match status:
        case 400:
            print('Bad request')
        case 400 | 401 | 403:
            return 'Not allowed'
        case 404:
            return 'Not found'
        case _:
            return "Something's wrong with the internet"


def for_func():
    for x in [1, 2, 3, 4]:
        print(x, x ** 2)

    # 遍历集合时修改集合的内容，会很容易生成错误的结果。
    # 因此不能直接进行循环，而是应遍历该集合的副本或创建新的集合：
    users: dict[str, str] = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    print(f'users -> {users}')
    for u, s in users.copy().items():
        if s == 'inactive':
            del users[u]
    print(f'users after del inactive user -> {users}')


# if
print_line("if")
if_func(5)

# match python3.10
print_line("match")
# None
print(match_func(400))
print(match_func(500))

# for
print_line('for')
for_func()
