from py_ads.ds.binary_tree import (BinaryTreeNode, find)


def test_find():
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(7)

    assert (find(root, 3) == root.left)
    assert (find(root, 9) is None)

    root.right = BinaryTreeNode(9)
    assert (find(root, 9) is not None)
