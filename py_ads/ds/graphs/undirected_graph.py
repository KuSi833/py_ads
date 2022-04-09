class UndirectedGraph:
    def __init__(self):
        self.map = dict()

    def adjacent(self, nodeA: str, nodeB: str):
        return nodeA in self.map[nodeB] and nodeB in self.map[nodeA]

    def add_node(self, node: str):
        self.map[node] = set()

    def remove_node(self, node: str):
        for edges in self.map.values():
            edges.discard(node)
        self.map.pop(node)

    def add_edge(self, nodeA: str, nodeB: str):
        self.map[nodeA].add(nodeB)
        self.map[nodeB].add(nodeA)

    def remove_edge(self, nodeA: str, nodeB: str):
        self.map[nodeA].remove(nodeB)
        self.map[nodeB].remove(nodeA)

    def get_neighbors(self, node: str):
        return self.map[node]
