from py_ads.ds.binary_tree import (BinaryTreeNode, find, size)


def create_tree():
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(7)
    return root


def test_find():
    root = create_tree()

    assert (find(root, 3) == root.left)
    assert (find(root, 9) is None)

    root.right = BinaryTreeNode(9)
    assert (find(root, 9) is not None)


def test_size():
    root = create_tree()

    assert (size(root) == 3)
