# Breadth First Search algorithm - means that, the bag is implemented as a FIFO stack.
# Mark vertices in increasing order of distance from s.
# Returned Spanning Tree (when run on vertex s)contains the shortest path to some vertex v,
# but it's not the Minimum Spanning Tree.
# Can also, set the distances of the rest of the vertex from the given s;
# when is single path the distance is 1, etc...

from collections import deque as dq


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






