#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq

def print_line(val: str, length=80):
    print(val.center(length, "*"))


print_line('dict for')
users: dict[str, str] = {'Hans': 'active',
                         'Éléonore': 'inactive',
                         '景太郎': 'active'}
print(f'users -> {users}')
# items() k,v
for u, s in users.copy().items():
    if s == 'inactive':
        del users[u]
print(f'users after del inactive user -> {users}')

print_line('check dict exists key')
# True
print('Hans' in users)
# False
print('zzf' in users)
