#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


def print_line(val: str, length=80):
    print(val.center(length, "*"))


a_deque = deque(range(1, 9, 2))
print(a_deque)
# right side
a_deque.append(11)
a_deque.pop()
# left side
a_deque.appendleft(0)
a_deque.popleft()
