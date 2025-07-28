import unittest
from typing import List, Tuple
from unittest import TestCase


def get_max_2(arr: List[int]) -> Tuple[int]:
    if len(arr) < 2:
        raise IndexError
    m1, m2 = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0],)
    for i in range(2, len(arr)):
        if arr[i] > m1:
            m2, m1 = m1, arr[i]
        elif arr[i] > m2:
            m2 = arr[i]
    return m1, m2


class Test(TestCase):
    def test_normal_case(self):
        max2: tuple[int] = get_max_2([1, 2, 3, 5, 4, -1, 100])
        self.assertEqual(max2, (100, 5))


if __name__ == '__main__':
    unittest.main()
