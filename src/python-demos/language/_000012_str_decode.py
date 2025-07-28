import unittest
from unittest import TestCase


class Test(TestCase):
    def test_normal_case(self):
        u8: str = '中国'
        u8e: bytes = u8.encode('utf-8')
        uc = u8e.decode('utf-8')
        uce = uc.encode()
        print(u8, u8e, uc)
        # unicode
        uc = u'中国'
        uce = uc.encode()
        u8 = uce.decode('utf-8')
        print(u8, u8e, uc)
        print('..sdfadf.mp4'.rstrip('.'))
        print(len(None))


if __name__ == '__main__':
    unittest.main()
