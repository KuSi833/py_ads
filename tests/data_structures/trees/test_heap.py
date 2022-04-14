from py_ads.ds.trees.binary_heap import MaxHeap, MinHeap
from typing import List


def test_max_heap():
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    assert (heap.extract_max() == 7)
    assert (heap.get_max() == 6)
    heap.insert(9)
    heap.insert(13)
    heap.insert(11)
    heap.insert(10)
    assert (heap.get_max() == 13)


def test_min_heap1():
    heap = MinHeap([4, 5, 8, 2])
    assert (heap.extract_min() == 2)


def test_min_heap2():
    heap = MinHeap([])
    heap.insert(-3)
    assert (heap.get_min() == -3)
    heap.insert(-2)
    heap.extract_min()
    assert (heap.get_min() == -2)
    heap.insert(-4)
    heap.extract_min()
    assert (heap.get_min() == -2)


if __name__ == "__main__":
    pass
