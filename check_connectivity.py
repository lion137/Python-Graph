# Randomized connectivity check on undirected graph (Aleliunas, Karp, Lipton, Lovasz, Rackoff, 79)
# Not very practical, but, still O(1) SPACE.


def are_connected(g, w, v):
    """Randomized algorithm for check connectivity in a given graph, doesn't need
    any additional memory storage, just few integers (memory O(1)). Time complexity
    O(number of vertices ^3) - so polynominal. When vertices aren't connected algrithm is exact -
    means return False with 100%, when are connected - returns True with probability of mistake
    0.1% - from Random Walks theory"""

    u = w # assign start vertex to u
    t = g.V # number of vertices
    for t in range(1000 * (t ** 3)):
        u = random.randint(g.adj_list(u)[0], g.adj_list(u)[-1]) # check random vertex from adjacency of u
        if u == v:
            return True
    return False
