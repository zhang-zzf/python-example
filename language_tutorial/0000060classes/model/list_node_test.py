#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from list_node import ListNode


class ListNodeTest(TestCase):
    def test_create_list_node(self):
        head = ListNode.new_list([1, 2, 3])
        self.assertEqual(2, head.next.val)


if __name__ == '__main__':
    unittest.main()
