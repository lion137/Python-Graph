# Minimum spanning tree as a another version of algorithms from "First Search" family;
# uses heap as a bag.
# Note: if all costs (map: E -> R+) are distinct we have the MST - the unique MST.
# Called Jarnik - Prim Algorithm.

import graphs_classes as gr
import BagMST as Bg


def cfs(g, s):
    """Minimum Spanning Tree (Cheapest First Search) algorithm: Takes a graph and vertex returns arrays of the cheapest
    edges, also mutates graph, to find connected components of given vertex"""
    edges = [None] * g.V  # Array of previous edges in the shortest s to v path.
    bag = Bg.MSTBag()
    for x in g.adj_list(s):
        bag.__add__(x)
    g.mark(s)
    while not bag.is_empty():
        tile = bag.pop()
        if not g.is_marked(tile[0]):
            g.mark(tile[0])
            edges[tile[0]] = tile
            for w in g.adj_list(tile[0]):
                if not g.is_marked(w[0]):
                    bag.__add__(w)
    return edges

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


if __name__ == '__main__':
    gr1 = gr.WeightedGraph(8)

    gr1.add_edge(0, 1, 2)
    gr1.add_edge(0, 4, 4)
    gr1.add_edge(0, 5, 1)
    gr1.add_edge(1, 2, 22)
    gr1.add_edge(1, 6, 67)
    gr1.add_edge(1, 5, 0)
    gr1.add_edge(2, 6, 8)
    gr1.add_edge(3, 7, 13)
    gr1.add_edge(4, 5, 10)
    gr1.add_edge(5, 6, 11)
    g = gr.WeightedGraph(4)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 0)
    g.add_edge(1, 2, 1)
    print("MST: ")
    gr2 = gr.WeightedGraph(3)
    gr2.add_edge(0, 1, 2)
    gr2.add_edge(1, 2, 3)
    print("Graph V_array: ", g.V_array)
    print("adjlist 0", g.adj_list(0))
    print(cfs_1(gr1, 0))
    print("Graph V_array: ", g.V_array)


'''from 0: [None, [1, 0], [2, 8], None, [4, 4], [5, 1], [6, 11], None] cfs
'''





