from typing import List, Any
from abc import ABC, abstractmethod


class MaxHeapADT(ABC):
    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def get_max(self) -> Any:
        "Returns the maximum element"
        pass

    @abstractmethod
    def delete_max(self) -> None:
        "Deletes the maximum element"

    @abstractmethod
    def extract_max(self) -> Any:
        "Removes and returns the maximum element."
        pass

    @abstractmethod
    def insert(self, element: Any) -> None:
        "Insert a new element."
        pass

    @abstractmethod
    def extract_max_and_insert(self, element: Any) -> None:
        "Extracts the maximum element and then inserts while sorting only once."
        pass

    # Knowledge of internal representaiton

    @abstractmethod
    def increase_key(self, i: int, decrement: Any) -> None:
        "Increase the value of an element."
        pass

    @abstractmethod
    def delete(self, i: int) -> None:
        "Deletes an element."
        pass


class MinHeapADT(ABC):
    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def get_min(self) -> Any:
        "Returns the minimum element"
        pass

    @abstractmethod
    def delete_min(self) -> None:
        "Deletes the minimum element"

    @abstractmethod
    def extract_min(self) -> Any:
        "Removes and returns the minimum element."
        pass

    @abstractmethod
    def insert(self, val: Any) -> None:
        "Insert a new element."
        pass

    @abstractmethod
    def extract_min_and_insert(self, element: Any) -> None:
        "Extracts the minimum element and then inserts while sorting only once."
        pass

    # Knowledge of internal representaiton

    @abstractmethod
    def decrease_key(self, i: int, decrement: Any) -> None:
        "Decrease the value of a key."
        pass

    @abstractmethod
    def delete(self, i: int) -> None:
        "Deletes an element."
        pass


class MaxHeap(MaxHeapADT):
    def __init__(self, initial: List[Any] = []) -> None:
        self.heap: List[Any] = initial
        self._heapify()

    def get_max(self) -> Any:
        return self.heap[0]

    def delete_max(self) -> None:
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

    def extract_max(self) -> Any:
        root = self.heap[0]
        # replace root with last element
        if len(self) >= 2:
            self.heap[0] = self.heap.pop()
            self._sift_down(0)
        else:
            self.heap.pop()
        return root

    def insert(self, val: Any):
        self.heap.append(val)
        self._sift_up(len(self) - 1)

    def extract_max_and_insert(self, val: Any):
        if val > self.root():
            return val
        root = self.root()
        self.heap[0] = val
        self._sift_down(0)
        return root

    # Knowledge of internal representation

    def increase_key(self, i: int, increment: Any) -> None:
        self.heap[i] += increment
        self._sift_up(i)

    def delete(self, i: int) -> None:
        self.increase_key(i, float('inf'))
        self.delete_max()

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

    def get_min(self) -> Any:
        return -self.heap.get_max()

    def delete_min(self) -> Any:
        self.heap.delete_max()

    def extract_min(self) -> Any:
        return -self.heap.extract_max()

    def extract_min_and_insert(self, val: Any):
        return -self.heap.extract_max_and_insert(-val)

    def insert(self, val: Any):
        self.heap.insert(-val)

    # Knowledge of internal representaiton
    def decrease_key(self, i: int, decrement: int):
        self.heap.increase_key(i, -decrement)

    def delete(self, i: int) -> None:
        self.decrease_key(i, -float("inf"))
        self.delete_min()

    # Internal
    def __len__(self) -> int:
        return self.heap.__len__()
