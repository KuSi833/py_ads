from py_ads.ds.graphs.undirected_weighted_graph import UndirectedWeightedGraph
from py_ads.ds.priority_queue import PriorityQueue
from py_ads.ds.disjoint_set import DisjointSet


def kruskals(graph: UndirectedWeightedGraph):
    # ADTs
    mst = set()
    dset = DisjointSet()
    pqueue = PriorityQueue()

    # Initialisation
    for node in graph.get_nodes():
        dset.make_set(node)
    for edge in graph.get_edges():
        pqueue.insert(edge, graph.get_edge_cost(*edge))

    # Algorithm
    while pqueue:
        _, (u, v) = pqueue.extractMin()
        if dset.find(u) != dset.find(v):
            mst.add((u, v))
            dset.union(u, v)

    return mst
