class DisjointSet:
    def __init__(self) -> None:
        self.parent = dict()
        self.rank = dict()

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 1

    def find(self, x):
        if self.parent[x] != x:
            # path compression
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:    # if equal found cycle
            # union by rank
            if self.rank[root_x] >= self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
                self.rank[root_y] = 0
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
                self.rank[root_x] = 0

    def __repr__(self) -> str:
        return (f"Edges: {self.parent.__repr__()}\n"
                f"Ranks: {self.rank.__repr__()}")
