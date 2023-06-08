import json
import unittest
from unittest import TestCase

mydict = {
    'name': '骆昊',
    'age': 38,
    'qq': 957658,
    'money': 3.555,
    'friends': ['王大锤', '白元芳'],
    'children': ('小张', '小红'),
    'cars': [
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
    ]
}


class Test(TestCase):
    def test_normal_case(self):
        try:
            with open('data.json', 'w', encoding='utf-8') as fs:
                json.dump(mydict, fs, ensure_ascii=False)
        except IOError as e:
            print(e)
        print('保存数据完成!')

    def test_json_str(self):
        print(mydict)
        print(json.dumps(mydict))
        json_str = json.dumps(mydict, ensure_ascii=False)
        print(json_str)
        json_obj = json.loads(json_str)
        print(type(json_obj))


if __name__ == '__main__':
    unittest.main()
