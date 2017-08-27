# Dijkstra algorithm to find the shortest paths in a graph; uses adjacency lists
# graph implementation and sys.maxisize as maximum distance


import graphs_classes as gr
import sys


def dijkstra(g, v):
    def min_dist(distance, short_path_set):
        minimum = sys.maxsize
        for v in g.V:
            if distance[v] < minimum and short_path_set[v] is False:
                minimum = distance[v]
                min_ind = v
        return min_ind

    dist = [sys.maxsize] * g.V
    dist[v] = 0
    short_path = [False] * g.V
    for cnt in range(g.V):
        w = min_dist(dist, short_path)
        short_path[w] = True
        for s in range(g.V):
            pass