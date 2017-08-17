# Arbitrary first search function (AFS) - on graph and vertex.
# Takes a graph G and a vertex s and returns all the nodes of the Graph reachable from s.
# This algorithm also check if graph is connected, finds connected components of s and, also,
# tests if s can reach given vertex t.
# As well as returns Spanning Tree (connected sub set of the edges of connected graph
#  which uses the all of the vertices) of connected components rooted in s;
# in the other words is minimum set of the edges connects the all vertices of G.
# A data structure a bag is just like a bag, doesn't return items in any
# particular order; there are more detailed implementations: dfs, bfs.

from graphs_classes import Graph as Gr
from Bag import Bag as Ba


def afs(g, s):
    """Arbitrary first search. Takes a graph G and vertex s and returns
    the all vertices connected to s - which is Spanned Tree
    rooted at s"""
    bag = Ba()
    bag.__add__(s)
    while bag.is_empty() is False:
        tile = bag.pick()
        if g.is_marked(tile) is False:
            g.mark(tile)
            for x in g.adj_list(tile):
                bag.__add__(x)
    return list(map(lambda z: z[0], filter(lambda y: y[1] if y[1] is True else False, g.V_array)))


def connected_vertices(g, s, v):
    """Tests if vertex v in the graph g is reachable from s;
    returns true if yes, false if not"""
    return True if v in afs(g, s) else False


def is_connected(g):
    """Checks if graf g is connected returns true or false"""
    return afs(g, 0) == list(range(g.V))


def all_connected_components(g):
    for v in range(g.V):
        if g.is_marked(v) is False:
            afs(g, v) # In fact any "First Search" can be plugged here.

if __name__ == '__main__':
    gr1 = Gr(8)

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

    gr2 = Gr(3)
    gr2.add_edge(0, 1)
    gr2.add_edge(1, 2)
    all_connected_components(gr1)
    print(gr1.V_array)








