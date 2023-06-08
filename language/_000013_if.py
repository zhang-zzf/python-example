import unittest
from unittest import TestCase


class Test(TestCase):
    def test_normal_case(self):
        a = ''
        if a:
            print(f'empty str is True')
        pass


if __name__ == '__main__':
    unittest.main()
