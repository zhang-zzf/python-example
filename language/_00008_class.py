import unittest
from abc import ABCMeta, abstractmethod
from typing import List, Union
from unittest import TestCase


class Person(object):
    """
    限定对象的属性
    """
    __slots__ = ['_name', '_age', '_gender', '__args', 'kwargs']

    # 构造函数
    def __init__(self, name: str, age: int, *args, **kwargs):
        # protected field
        self._name = name
        self._age = age
        # private field
        self.__args = args
        # public field
        self.kwargs = kwargs

    def __str__(self) -> str:
        return f'{{"name": "{self.__name}", "age": {self.__age}}}'

    def watch_tv(self):
        if self.__is_adult():
            print(f'{self.__name} is watching 91porn')
        else:
            print(f'{self.__name} is watching "<<熊出没>>"')

    @property
    def name(self) -> int:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    # 静态方法
    @staticmethod
    def is_child(age: int) -> bool:
        return age < 12

    # 类方法，第一个参数是类本身
    @classmethod
    def build(cls, name: str, age: int):
        return cls(name, age)

    # private method
    def __is_adult(self):
        return self.__age > 18


class Student(Person):

    def __init__(self, name: str, age: int, grade: str):
        super.__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nick_name=None):
        self._nick_name = nick_name

    @abstractmethod
    def make_noice(self):
        pass

    def health(self):
        print(f"{self._nick_name} is health")


# Inheritance
class Cat(Pet):

    def make_noice(self):
        print(f'{self._nick_name}-> 喵喵喵')


# Inheritance
class Dog(Pet):
    def make_noice(self):
        print(f'{self._nick_name}-> 汪汪汪')


class Test(TestCase):
    def test_normal_case(self):
        self.assertEqual(str(Person('zhang.zzf', '34')), '{"name": "zhang.zzf", "age": 34}')

    def test_normal_case_use(self):
        stu: Person = Person('zhang.zzf', 17)
        stu.watch_tv()
        self.assertEqual(stu.name, 17)
        stu.name = 28
        self.assertEqual(stu.name, 28)
        self.assertEqual(Person.is_child(11), True)
        self.assertEqual(Person.build('zhang.zf', 18).name, 18)

    def test_abstract_class(self):
        pets: List[Pet] = [Dog('dog1'), Cat('cat1'), Dog('dog2')]
        # Polymorphism
        for pet in pets:
            pet.make_noice()
            pet.health()


if __name__ == '__main__':
    unittest.main()
