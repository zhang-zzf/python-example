# data types in python

## int / float

```python
int(float('5.6'))
int(5.6)
```

## str

```python
a_str = 'Hello'
a_str2 = "Hello"
a_str3: str = '''
    hello, World
'''
```

## bool

```python
a_true: bool = True
a_false: bool = False
# False, True
print(bool(0), bool(1))
# False, True
print(bool(''), bool(' '))
```

## list

```python
a_list = []
a_list_2: list[int] = [1, 2, 3]
```

### 列表推导式

```python
from math import pi

# 表达式 for if
# 表达式表示要对每个元素做的事情
# for 表示要操作的基础列表的范围
# if 表示对基础列表的过滤
a_squares_2 = [x ** 2 for x in range(10)]
a_squares_3 = [x ** 2 for x in range(10) if x % 2 != 0]
pi_list = [str(round(pi, i)) for i in range(1, 6)]
```

### 双端操作

```python
a_list: list[int] = [0]

# add to the tail
a_list.append(1)
# delete from the tail
a_list.pop()

# add to the head
a_list.insert(0, -1)
# delete from the head
a_list.pop(0)
```

#### Lists Using as Queues

You can use Lists as Queues. Lists are not efficient for using as Queues.

```python
a_queue: list[int] = []
# enqueue
a_queue.append(1)
# dequeue
a_queue.pop(0)
```

To implement a queue, use collections.deque

```python
from collections import deque

a_deque = deque(range(1, 9, 2))
print(a_deque)
# right side
a_deque.append(11)
a_deque.pop()
# left side
a_deque.appendleft(0)
a_deque.popleft()

```

#### Lists Using as Stacks

```python
a_stack: list[int] = []
# push
a_stack.append(1)
# pop
a_stack.pop()
```

## dict

字典以 关键字 为索引，关键字通常是字符串或数字，也可以是其他任意**不可变类型**。

```python
a_dict: dict[str, int] = {'jack': 4098, 'sape': 4139}
a_dict['guido'] = 4127
jack_number: int = a_dict['jack']
del a_dict['jack']

```
