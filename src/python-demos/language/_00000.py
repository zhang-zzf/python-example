import os
import time
from concurrent.futures import ThreadPoolExecutor
from time import sleep

a = int(input("a= "))
b = int(input('b= '))
# 字符串格式化
print('%d + %d = %d' % (a, b, (a + b)))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, (a / b)))
print('%d %% %d = %d' % (a, b, a % b))
# 整除
print('%d // %d = %d' % (a, b, a // b))
# 指数运算
print('%d ** %d = %d' % (a, b, a ** b))


def funcA():
    time.sleep(30)
    print(f'thread pid: {os.getpid()}')


with ThreadPoolExecutor(2) as executor:
    for i in range(2):
        executor.submit(funcA)
    print(f'main pid: {os.getpid()}')

