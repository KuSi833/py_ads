from py_ads.ds.graphs.undirected_weighted_graph import UndirectedWeightedGraph
from py_ads.ds.priority_queue import PriorityQueue


def prims(graph: UndirectedWeightedGraph):
    # ADTs
    pqueue = PriorityQueue()
    visited = set()
    weight = dict()
    mst = set()

    # Initialisation
    nodes = graph.get_nodes()
    for node in nodes:
        weight[node] = float("inf")
    source = nodes[0]
    pqueue.insert(source, 0)
    visited.add(source)

    # Algorithm
    while pqueue:
        cost, current = pqueue.extractMin()
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                newCost = cost + graph.get_edge_cost(current, neighbor)
                if newCost < weight[neighbor]:
                    visited.add(neighbor)
                    pqueue.insert(neighbor, newCost)
                    weight[neighbor] = newCost
                    mst.add((current, neighbor))
    return mst
