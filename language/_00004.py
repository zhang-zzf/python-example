import json
import sys

list1 = []
list2 = [1, 2]

for idx in range(len(list2)):
    print(idx, '->', list2[idx])

for item in list2:
    print(item)

for idx, item in enumerate(list2):
    print(idx, ":", item)

# 追加元素
list2.append(3)
list2.insert(0, 0)
print(list2)

# 删除元素
if 5 in list2:
    list2.remove(5)

list2.pop(-1)
print(list2)

# 合并操作
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)

# sort
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)

# sorted 函数不修改入参
list3 = [1, 2, 3]
print(sorted(list3, reverse=True), list3)

#
f1 = fruits.copy()
f2 = fruits[:]

# 列表
list4 = [x * x for x in range(100)]
print(type(list4), '->', list4)
print(type(list4), 'size->', sys.getsizeof(list4))

# 函数
func = (x * x for x in range(100))
print(type(func), '->', func)
print(type(func), 'size->', sys.getsizeof(func))
# Iterate
for x in func:
    pass
# convert to list
list5 = list(func)

# 元组
tuple1 = (1, 2, 3)
list6 = list(tuple1)
tuple2 = tuple(list6)
print(tuple1, list6, tuple2, sep='\n')

# 集合
print('set'.center(80, '*'))
print({1, 1, 2, 3}, set([1, 1, 2, 3]))
print({x for x in range(10) if x % 3 == 0})
set1 = set((1, 2, 3))
print(set1.pop(), set1.pop(), set1)
set1 = set((1, 2, 3))
set1.add(3)
print(set1.discard(5), set1)
print(set1.discard(1), set1, set1.union([1, 5]))

# 字典
print('dict'.center(80, '+'))
print({'骆昊': 95, '白元芳': 78, '狄仁杰': 82}, dict(a=97, b=98))
print({x: x * x for x in range(10) if x % 2 == 0})
dict1 = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# 默认遍历 key
for key in dict1:
    print(key, ":", dict1[key])
# 遍历 value
for val in dict1.values():
    print(val)
# 遍历 key, value
for k, v in dict1.items():
    print(k, '->', v)

dict1['骆昊'] = 199
print(dict1['骆昊'], dict1.update({'骆昊': 88}), dict1.get('骆昊'))
print(dict1.pop('骆昊'), dict1.get('骆昊'), dict1.get('NotExist'))

# dict['NotExistKey'] will raise Error
# dict.get('NotExistKey') will return None

set2 = set({"91视频"})
json_set = json.dumps([x for x in set2])
json_set2 = json.dumps([x for x in set2], ensure_ascii=False)
set_from_json = json.loads(json_set)
print(set_from_json)

with open('a') as file:
    file.write()
