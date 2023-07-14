# define a class
class MyClass01:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    PI = 3.14
    msg = 'Hello, World'


class Complex(object):
    # constructor
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    # toString()
    def __str__(self):
        return f'{{"r": {self.r}, "i": {self.i}}}'


if __name__ == '__main__':
    print(MyClass01.msg)
