from typing import List, Any


class MaxHeap():
    def __init__(self, initial: List[Any] = []) -> None:
        self.heap: List[Any] = initial
        self._sift_down(0)

    def find_max(self) -> Any:
        return self.heap[0]

    def extract_max(self) -> Any:
        max = self.heap[0]
        # replace root with last element
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max

    def increase_key(self, i: int, increment: Any) -> None:
        self.heap[i] += increment
        self._sift_up(i)

    def insert(self, val: Any):
        self.heap.append(val)
        self._sift_up(len(self) - 1)

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
