from py_ads.ds.trees.heap import MaxHeap


def test_heap():
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    assert (heap.extract_max() == 7)
    assert (heap.find_max() == 6)
    heap.insert(9)
    heap.insert(13)
    heap.insert(11)
    heap.insert(10)
    assert (heap.find_max() == 13)


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    print(heap.extract_max())
    heap.insert(9)
    heap.insert(13)
    heap.insert(11)
    heap.insert(10)
    print(heap.extract_max())
