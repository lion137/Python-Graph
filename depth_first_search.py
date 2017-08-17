# Depth First Search implemented as a function.
# Data structure used as a bag is LIFO stack, implemented in compiler
# via recursion. Of course when exceed stack capacity, we can use stack explicitly,
# like in the other versions

from graphs_classes import Graph as Gr
import arbitrary_first_search as afs


def dfs(g, v):
    if g.is_marked(v) is False:
        g.mark(v)
        print("in dfs", v)
        for w in g.adj_list(v):
            dfs(g, w)

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

    g = Gr(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(gr1.V_array)
    dfs(g, 2)
    print(gr1.V_array)


