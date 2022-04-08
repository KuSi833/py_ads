from collections import deque

from py_ads.ds.graphs.undirected_graph import UndirectedGraph


def ShortestPathBFS(graph: UndirectedGraph, start, end):
    def get_path(node, parent_dict):
        path = []
        while parent_dict[node] != node:
            path.append(node)
            node = parent_dict[node]
        path.append(node)
        path.reverse()
        return path

    q = deque([(start, start, 0)])
    parent_dict = dict()
    while q:
        current, parent, cost = q.popleft()
        parent_dict[current] = parent
        if current == end:
            return "->".join(get_path(current, parent_dict))
        else:
            for neighbor in graph.get_neighbors(current):
                if neighbor not in parent_dict:
                    q.append((neighbor, current, cost + 1))
    return "-1"
