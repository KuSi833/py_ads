from typing import List
from py_ads.types import Value


class BinaryTreeNode:
    def __init__(self, val: Value, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find(node: BinaryTreeNode, val):
    if node:
        if node.val == val:
            return node
        return find(node.left, val) or find(node.right, val)


def size(node: BinaryTreeNode):
    if node:
        return 1 + size(node.left) + size(node.right)
    return 0
