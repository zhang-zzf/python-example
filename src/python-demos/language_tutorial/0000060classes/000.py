# TODO 类定义过程中使用注解引用类本身
from __future__ import annotations

from typing import List, Optional

from model.classes import MyClass01, Complex


class TreeNode:

    def __init__(self, val: int = 0,
                 left: TreeNode = None,
                 right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

    # TODO 类方法
    # @classmethod 表示的函数为类方法
    # 类方法的第一个参数为 cls （类本身），可以使用 cls() 来创建类实例
    # TODO Optional[TreeNode]
    # Optional[X] is equivalent to X | None
    @classmethod
    def decode(cls, nodes: List[int]) -> Optional[TreeNode]:
        if len(nodes) == 0:
            return None
        root = cls(nodes.pop(0))
        level = [root]
        while len(level) > 0:
            r = level.pop(0)
            if not r:
                continue
            left_filled: bool = False
            for i in range(min(2, len(nodes))):
                n = nodes.pop(0)
                # TODO 三目运算符
                node = cls(n) if n else None
                if not left_filled:
                    r.left = node
                    left_filled = True
                else:
                    r.right = node
                level.append(node)
        return root

    # TODO 静态方法
    @staticmethod
    def encode() -> None:
        pass


if __name__ == '__main__':
    mc1 = MyClass01()
    print(mc1.x)
    print(Complex(3.0, -4.5))
    TreeNode.encode()
    TreeNode().encode()
