import unittest
from unittest import TestCase


def open_file_as_txt():
    try:
        with open('_00008_class.py') as file:
            # 默认以文本方式打开文件，读出的文件内容保存为字符串类型
            read: str = file.read()
            print(type(read))
    except FileNotFoundError:
        pass
    except LookupError:
        pass
    except UnicodeDecodeError:
        pass


def open_file_as_binary():
    try:
        with open('_00008_class.py', 'rb') as file:
            read: bytes = file.read()
            print(type(read))
    except IOError:
        pass


class Test(TestCase):
    def test_normal_case(self):
        open_file_as_txt()

    def test_normal_case_1(self):
        open_file_as_binary()


if __name__ == '__main__':
    unittest.main()
