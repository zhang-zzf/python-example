# TODO 类定义过程中使用注解引用类本身
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    sex: str

def main():
    p = Person(name="zhang.zzf", age=18, sex='male')
    p = Person(name=18, age=18, sex='male')
    print(p)
    pass


if __name__ == '__main__':
    main()