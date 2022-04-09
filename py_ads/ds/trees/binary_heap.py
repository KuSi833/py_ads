from typing import List, Any
from abc import ABC, abstractmethod


class HeapADT(ABC):
    @abstractmethod
    def root(self) -> Any:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

    @abstractmethod
    def push(self, val: Any):
        pass

    @abstractmethod
    def pushpop(self, val: Any):
        pass


class MaxHeapADT(HeapADT):
    @abstractmethod
    def increase_key(self, i: int, increment: Any) -> None:
        pass


class MinHeapADT(HeapADT):
    @abstractmethod
    def decrease_key(self, i: int, decrement: Any) -> None:
        pass


class MaxHeap(MaxHeapADT):
    def __init__(self, initial: List[Any] = []) -> None:
        self.heap: List[Any] = initial
        self._heapify()

    def root(self) -> Any:
        return self.heap[0]

    def pop(self) -> Any:
        root = self.heap[0]
        # replace root with last element
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def increase_key(self, i: int, increment: Any) -> None:
        self.heap[i] += increment
        self._sift_up(i)

    def push(self, val: Any):
        self.heap.append(val)
        self._sift_up(len(self) - 1)

    def pushpop(self, val: Any):
        if val > self.root():
            return val
        root = self.root()
        self.heap[0] = val
        self._sift_down(0)
        return root

    # Internal

    def __len__(self) -> int:
        return self.heap.__len__()

    def _left_child(self, i: int) -> int:
        return (2 * i) + 1

    def _right_child(self, i: int) -> int:
        return (2 * i) + 2

    def _parent(self, i: int) -> int:
        return int((i - 1) / 2)

    def _sift_down(self, i: int):
        largest = i
        left, right = self._left_child(i), self._right_child(i)

        if left < len(self) and self.heap[largest] < self.heap[left]:
            largest = left

        if right < len(self) and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(largest)

    def _sift_up(self, i: int):
        parent = self._parent(i)
        if parent >= 0 and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._sift_up(parent)

    def _heapify(self):
        start = self._parent(len(self) - 1)
        for i in range(start, -1, -1):
            self._sift_down(i)


class MinHeap(MinHeapADT):
    def __init__(self, initial: List[Any] = []) -> None:
        self.heap = MaxHeap([-num for num in initial])

    def __len__(self) -> int:
        return self.heap.__len__()

    def decrease_key(self, i: int, decrement: int):
        self.heap.increase_key(i, -decrement)

    def pop(self) -> Any:
        return -self.heap.pop()

    def push(self, val: Any):
        self.heap.push(-val)

    def pushpop(self, val: Any):
        return -self.heap.pushpop(-val)

    def root(self) -> Any:
        return -self.heap.root()
