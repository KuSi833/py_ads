from py_ads.ds.graphs.undirected_weighted_graph import UndirectedWeightedGraph
from py_ads.algos.kruskals import kruskals
from py_ads.algos.prims import prims

# def test_minimum_spanning_tree():

graph = UndirectedWeightedGraph()

for u, v, cost in [
    ("Hamburg", "Frankfurt", 1),
    ("Hamburg", "Berlin", 2),
    ("Berlin", "Bonn", 5),
    ("Berlin", "Magdeburg", 1),
    ("Frankfurt", "Magdeburg", 3),
    ("Frankfurt", "Bonn", 3),
    ("Magdeburg", "Chemitz", 1),
    ("Bonn", "Chemitz", 3),
    ("Bonn", "Karlsruhe", 2),
    ("Bonn", "Munich", 5),
    ("Chemitz", "Munich", 4),
    ("Karlsruhe", "Munich", 3),
]:
    graph.add_edge(u, v, cost)


def evaluate_mst(mst):
    total_weight = 0
    for u, v in mst:
        total_weight += graph.get_edge_cost(u, v)
        print(f"{u} -> {v}")
    print(f"Total weight: {total_weight}")


evaluate_mst(kruskals(graph))
print("")
evaluate_mst(prims(graph))
