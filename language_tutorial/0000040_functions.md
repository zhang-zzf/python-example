# functions in python

## parameters / arguments

```python
# 表示 接受 arg1, 0 到 n 个位置参数，0 到 n 个 keyword 参数
def a_func(arg1: int, *args, **kwargs):
    # args is a tuple
    # kwargs is a dict
    pass


# arg1, 2 position args
a_func(1, 2, "2")
a_func(1)
# arg1, 1 keyword args
a_func(1, a="a")
a_func(arg1=1, a="a")
# arg1, 2 position args, 1 keyword args
a_func(1, 2, 3, a="a")
```

### list/dick unpacking

```python
# 表示 接受 arg1, 0 到 n 个位置参数，0 到 n 个 keyword 参数
def a_func(arg1: int, *args, **kwargs):
    # args is a tuple
    # kwargs is a dict
    pass


# a_list = [3,4,5]
a_list = list(range(3, 6))
# arg1, 3 position args
a_func(1, *a_list)

# arg1, 2 keyword args
a_dict = {"a": "a", "b": "b"}
a_func(1, **a_dict)

a_func(1, *a_list, **a_dict)
```

## anonymous functions

python 支持使用 `lambda` 表达式定义匿名函数

```python
# lambda 仅支持一个表达式
func = lambda x, y, z: x * y - z
```