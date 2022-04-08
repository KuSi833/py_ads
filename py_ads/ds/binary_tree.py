class BinaryTreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find(node: BinaryTreeNode, val):
    if node:
        if node.val == val:
            return node
        return find(node.left, val) or find(node.right, val)
