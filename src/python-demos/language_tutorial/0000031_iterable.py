#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict


def print_line(val: str, length=80):
    print(val.center(length, "*"))


class MyList:
    def __init__(self, data: list):
        self.data = data

    """
    __getitem__ -> MyList is iterable
    """

    def __getitem__(self, idx):
        return self.data[idx]


my_list = MyList([1, 2, 3])
it = iter(my_list)
print(f"iter(my_list) -> {type(it)}")
for i in it:
    print(i)

print_line("Iterator")


class MyList2:
    def __init__(self, data: list):
        self.data = data

    """
    返回 MyList2 的 Iterator 对象
    """
    def __iter__(self):
        return MyList2Iterator(self)


class MyList2Iterator:
    def __init__(self, data: MyList2):
        self.my_list2 = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.my_list2.data):
            raise StopIteration
        else:
            self.index += 1
            return self.my_list2.data[self.index - 1]

    """
    使迭代器本身可迭代
    """
    def __iter__(self):
        return self


my_list_2 = MyList2([1, 2, 3])
for i in my_list_2:
    print(i)

# for i in my_list_2:
#    print(i)
# 的实现如下:
it = my_list_2.__iter__()
while True:
    try:
        print(it.__next__())
    except StopIteration:
        break

print_line("Iterate by __iter__()")
iter_it = iter(my_list_2)
print(f"iter(my_list2) -> {type(iter_it)}")
print(f"iter(my_list2).id() -> {id(iter_it)}")
it = my_list_2.__iter__()
print(f"my_list2.__iter__() -> {type(it)}")
print(f"my_list2.__iter__().id() -> {id(it)}")

print_line("next(Iterator)")
while True:
    try:
        print(f"next(Iterator) -> {next(it)}")
    except StopIteration:
        break

print_line("Iterator.__iter__()")
it = iter(my_list_2)
for i in it:
    print(i)
