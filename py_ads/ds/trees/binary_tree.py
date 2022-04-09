from py_ads.types import Value


class BinaryTreeNode:
    def __init__(self, val: Value, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find(node: BinaryTreeNode, val: Value):
    if node:
        if node.val == val:
            return node
        return find(node.left, val) or find(node.right, val)


def size(node: BinaryTreeNode):
    if node:
        return 1 + size(node.left) + size(node.right)
    return 0


# Traversals
def preorder(node: BinaryTreeNode):
    if node:
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node: BinaryTreeNode):
    if node:
        preorder(node.left)
        print(node.val, end=" ")
        preorder(node.right)


def postorder(node: BinaryTreeNode):
    if node:
        preorder(node.left)
        preorder(node.right)
        print(node.val, end=" ")
