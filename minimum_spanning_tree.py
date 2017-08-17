# Minimum spanning tree as a another version of algorithms from "First Search" family;
# uses heap as a bag.
# Note: if all costs (map: E -> R+) are distinct we have the MST - the unique MST.
# Called Jarnik - Prim Algorithm.

import BagMST as Bg


def cfs_1(g, s):
    """Minimum Spanning Tree (Cheapest First Search) algorithm: Takes a graph and vertex returns arrays of the cheapest
    edges, also mutates graph, to find connected components of given vertex"""
    edges = []  # Array of previous edges in the shortest s to v path.
    bag = Bg.MSTBag()
    for x in g.adj_list(s):
        bag.__add__(x)
    g.mark(s)
    while not bag.is_empty():
        tile = bag.pop()
        if not g.is_marked(tile[0]):
            g.mark(tile[0])
            edges.append(tile[0])
            if tile[0] == 6:
                return edges
            for w in g.adj_list(tile[0]):
                if not g.is_marked(w[0]):
                    bag.__add__(w)
    return edges







