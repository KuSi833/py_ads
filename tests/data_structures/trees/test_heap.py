from py_ads.ds.trees.binary_heap import MaxHeap, MinHeap
from typing import List


def test_max_heap():
    heap = MaxHeap()
    heap.push(5)
    heap.push(6)
    heap.push(7)
    assert (heap.pop() == 7)
    assert (heap.root() == 6)
    heap.push(9)
    heap.push(13)
    heap.push(11)
    heap.push(10)
    assert (heap.root() == 13)


def test_min_heap1():
    heap = MinHeap([4, 5, 8, 2])
    assert (heap.pop() == 2)


def test_min_heap2():
    heap = MinHeap([])
    heap.push(-3)
    assert (heap.root() == -3)
    heap.push(-2)
    heap.pop()
    assert (heap.root() == -2)
    heap.push(-4)
    heap.pop()
    assert (heap.root() == -2)


if __name__ == "__main__":
    pass
