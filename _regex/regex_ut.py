import unittest
import re
from typing import Pattern
from unittest import TestCase


class Test(TestCase):

    '''
    # 使用 pattern 和 text 匹配
    match: re.Match = re.match('(w+)\.(\w+)', text)
    '''

    def test_givenReSearch_whenIgnoreCase_then(self):
        text: str = 'www.baidu.com'
        # search 扫描整个字符串并返回第一个成功的匹配
        match: re.Match = re.search('Baidu', text)
        self.assertIsNone(match)
        # re.I 或者 re.IGNORECASE 忽略大小写
        # 多个 flag 使用 `|` 连接
        match: re.Match = re.search('Baidu', text, re.IGNORECASE | re.I)
        self.assertIsNotNone(match)

    def test_givenReSearch_when_then(self):
        text: str = 'www.baidu.com'
        # search 扫描整个字符串并返回第一个成功的匹配
        match: re.Match = re.search('baidu', text)
        self.assertIsNotNone(match)

    # 测试方法必须以 test 开头
    def test_givenReMatch_whenNotMatch_then(self):
        text: str = 'www.baidu.com'
        # match 从第 0 位开始匹配
        match: re.Match = re.match('baidu', text)
        self.assertEqual(match, None)

    def test_givenReMatch_normal_case(self):
        text: str = 'www.baidu.com'
        # match 从第 0 位开始匹配
        match: re.Match = re.match('(w+)\.(\w+)', text)
        pattern: Pattern = re.compile('(w+)\.(\w+)')
        self.assertEqual(match.re, pattern)
        self.assertEqual(match.string, text)
        # match.group() 返回匹配到的字符串
        self.assertEqual(match.group(), 'www.baidu')
        self.assertEqual(match.group(1), 'www')
        self.assertEqual(match.group(2), 'baidu')
        self.assertEqual(match.span(2), (4, 9))
        # match.groups() 返回匹配到的字符串列表
        # 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
        # Return a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern.
        self.assertEqual(match.groups(), ('www', 'baidu'))


if __name__ == '__main__':
    unittest.main()
