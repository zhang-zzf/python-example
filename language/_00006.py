import unittest
from unittest import TestCase


def get_file_suffix(filename: str, need_dot: bool = None) -> str:
    need_dot = True if need_dot is None else need_dot
    pos = filename.rfind('.')
    if -1 < pos < len(filename) - 1:
        idx = pos if need_dot else pos + 1
        return filename[idx:]
    else:
        raise IndexError()


class Test(TestCase):
    def test_get_file_suffix_normal_case(self):
        file_suffix = get_file_suffix('222.aa.mp4')
        self.assertEqual(file_suffix, '.mp4')

    def test_get_file_suffix_case_1(self):
        with self.assertRaises(IndexError):
            get_file_suffix('aaa')

    def test_get_file_suffix_case_2(self):
        with self.assertRaises(IndexError):
            get_file_suffix('aaa.')


if __name__ == '__main__':
    unittest.main()
