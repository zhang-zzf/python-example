from unittest import TestCase

import math_util as mu


class Test(TestCase):
    def test_fib(self):
        fib = mu.fib(3)
        if 2 not in fib:
            self.fail()
