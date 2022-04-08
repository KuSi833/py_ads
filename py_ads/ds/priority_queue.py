import heapq


class PriorityQueue:
    def __init__(self, initial=[]) -> None:
        self.heap = initial
        heapq.heapify(self.heap)

    def insert(self, element, priority):
        heapq.heappush(self.heap, (priority, element))

    def extractMin(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)

    def __repr__(self) -> str:
        return self.heap.__repr__()