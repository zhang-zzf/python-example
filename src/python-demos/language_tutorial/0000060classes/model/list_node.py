#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类定义过程中使用注解引用类本身
from __future__ import annotations

from typing import Optional


class ListNode:
    @classmethod
    def new_list(cls, nodes: list[int]) -> Optional[ListNode]:
        if nodes is None or len(nodes) == 0:
            return None
        head = None
        for x in reversed(nodes):
            head = ListNode(x, head)
        return head

    def __init__(self, val=0, next_node: ListNode = None):
        self.val = val
        self.next = next_node

    # toString()
    def __str__(self) -> str:
        return f'{{"val": {self.val}}}'


if __name__ == '__main__':
    a_list_node = ListNode(5)
    print(a_list_node.val)
    print(a_list_node)
