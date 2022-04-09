class WeightedGraph:
    def __init__(self):
        self.map = dict()
        self.weight = dict()

    def adjacent(self, nodeA: str, nodeB: str):
        return nodeA in self.map[nodeB] and nodeB in self.map[nodeA]

    def add_node(self, node: str):
        self.map[node] = set()

    def remove_node(self, node: str):
        for edges in self.map.values():
            edges.discard(node)
        self.map.pop(node)

    def get_nodes(self):
        return self.map.keys()

    def add_edge(self, nodeA: str, nodeB: str, cost: float):
        if nodeA not in self.map:
            self.add_node(nodeA)
        if nodeB not in self.map:
            self.add_node(nodeB)
        self.map[nodeA].add(nodeB)
        self.weight[nodeA, nodeB] = cost

    def remove_edge(self, nodeA: str, nodeB: str):
        self.map[nodeA].remove(nodeB)
        self.weight.pop(nodeA, nodeB)

    def get_neighbors(self, node: str):
        return self.map[node]

    def get_edge_cost(self, nodeA: str, nodeB: str):
        return self.weight[nodeA, nodeB]
