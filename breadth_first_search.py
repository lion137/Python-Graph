# Breadth First Search algorithm - means that, the bag is implemented as a FIFO stack.
# Mark vertices in increasing order of distance from s.
# Returned Spanning Tree (when run on vertex s)contains the shortest path to some vertex v,
# but it's not the Minimum Spanning Tree.
# Can also, set the distances of the rest of the vertex from the given s;
# when is single path the distance is 1, etc...

from collections import deque as dq
from graphs_classes import Graph as Gr
from graphs_classes import SortedGraph as Sg


def bfs_1(g, s):
    bag = dq()
    bag.append(s)
    while bag:
        tile = bag.popleft()
        if g.is_marked(tile) is False:
            g.mark(tile)
            for w in g.adj_list(tile):
                bag.append(w)


def bfs(g, s):
    """Takes a graph and returns arrays of dist and edges, also mutates graph, to find
    connected components of given vertex"""
    dist = [None] * g.V  # Distances to s for every node in Spanning Tree.
    edges = [None] * g.V  # Array of previous edges in the shortest s to v path.
    bag = dq()
    bag.append(s)
    dist[s] = 0
    while bag:
        tile = bag.popleft()
        if g.is_marked(tile) is False:
            g.mark(tile)
            for w in g.adj_list(tile):
                if g.is_marked(w) is False:
                    dist[w] = dist[tile] + 1
                    edges[w] = tile
                    bag.append(w)

    return dist, edges


gr2 = Gr(3)
gr2.add_edge(0, 1)
gr2.add_edge(1, 2)


gr1 = Sg(8)

gr1.add_edge(0, 1)
gr1.add_edge(0, 4)
gr1.add_edge(0, 5)
gr1.add_edge(1, 2)
gr1.add_edge(1, 6)
gr1.add_edge(1, 5)
gr1.add_edge(2, 6)
gr1.add_edge(3, 7)
gr1.add_edge(4, 5)
gr1.add_edge(5, 6)
# print(gr1.V_array)
tmp = bfs(gr1, 0)
print(tmp)
print(gr1.V_array)
'''([0, 1, 2, None, 1, 2, 3, None], [None, 0, 1, None, 0, 4, 2, None])
[[0, True], [1, True], [2, True], [3, False], [4, True], [5, True], [6, True], [7, False]]'''




