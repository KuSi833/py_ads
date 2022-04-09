from py_ads.ds.graphs.undirected_graph import UndirectedGraph
from py_ads.algos.shortest_path_bfs import ShortestPathBFS


def test_shortest_path_bfs():

    graph = UndirectedGraph()
    for node in ["Hamburg", "Frankfurt", "Berlin", "Magdeburg", "Chemitz", "Bonn", "Karlsruhe", "Munich"]:
        graph.add_node(node)

    for a, b in [
        ("Hamburg", "Frankfurt"),
        ("Hamburg", "Berlin"),
        ("Frankfurt", "Magdeburg"),
        ("Berlin", "Bonn"),
        ("Berlin", "Magdeburg"),
        ("Magdeburg", "Chemitz"),
        ("Bonn", "Chemitz"),
        ("Bonn", "Karlsruhe"),
        ("Bonn", "Munich"),
        ("Chemitz", "Munich"),
    ]:
        graph.add_edge(a, b)

    graph.remove_node("Bonn")
    graph.remove_edge("Berlin", "Magdeburg")

    assert (ShortestPathBFS(graph, "Berlin", "Munich") == "Berlin->Hamburg->Frankfurt->Magdeburg->Chemitz->Munich")
    assert (ShortestPathBFS(graph, "Hamburg", "Karlsruhe") == "-1")
