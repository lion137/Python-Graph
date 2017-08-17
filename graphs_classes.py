# Simple graph API in Python, implementation uses adjacent lists.
# Classes: Graph - simple undirected, unweighted graph, SortedGraph -
# undirected graph, with adjacent lists sorted, WeightedGraph -
# undirected, weighted graph.
# Usage:
# Creating new graph: gr1 = Graph(v) - creates new
# graph with no edges and v vertices;


from sortedcollections import SortedList as Sl


class Graph:
    """Class graph, creates a graph - described by integers - number
    of vertices - V : v0, v1, ..., v(V-1)"""

    def __init__(self, v_in):
        """constructor -  takes number of vertices and creates a graph
         with no edges (E = 0) and an empty adjacent lists of vertices"""
        self.V = v_in
        _array = [x for x in zip(range(v_in), [False] * v_in)]
        self.V_array = []
        for x in _array:
            self.V_array.append(list(x))
        self.E = 0
        self.adj = []
        for i in range(v_in):
            self.adj.append([])

    def V(self):
        """returns number of vertices"""
        return self.V

    def E(self):
        """returns number of edges"""
        return self.E

    def add_edge(self, v, w):
        """adds an edge to the graph, takes two integers (two vertices)
         and creates an edge v,w - by modifying appropriate adjacent lists """
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def adj_list(self, v):
        """Takes an integer - a graph vertex and returns the adjacency lists of it"""
        return self.adj[v]

    def mark(self, v):
        self.V_array[v][1] = True

    def is_marked(self, v):
        if self.V_array[v][1] is True:
            return True
        else:
            return False

    def __str__(self):
        """to string method, prints the graph"""
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + " "
            s += "\n"
        return s


class SortedGraph:

    """Class sorted graph, creates a graph - described by integers - number
    of vertices - V : v0, v1, ..., v(V-1); using sorted adjacency lists implementation"""

    def __init__(self, v_in):
        """constructor -  takes number of vertices and creates a graph
         with no edges (E = 0) and an empty adjacent lists of vertices"""
        self.V = v_in
        _array = [x for x in zip(range(v_in), [False] * v_in)]
        self.V_array = []
        for x in _array:
            self.V_array.append(list(x))
        self.E = 0
        self.adj = Sl()
        for i in range(v_in):
            self.adj.add(Sl())

    def V(self):
        """returns number of vertices"""
        return self.V

    def E(self):
        """returns number of edges"""
        return self.E

    def add_edge(self, v, w):
        """adds an edge to the graph, takes two integers (two vertices)
         and creates an edge v,w - by modifying appropriate adjacent lists """
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def adj_list(self, v):
        """Takes an integer - a graph vertex and returns the adjacency lists of it"""
        return self.adj[v]

    def mark(self, v):
        self.V_array[v][1] = True

    def is_marked(self, v):
        if self.V_array[v][1] is True:
            return True
        else:
            return False

    def __str__(self):
        """to string method, prints the graph"""
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + " "
            s += "\n"
        return s


class WeightedGraph:
    """Class graph, creates a graph - described by integers - number
    of vertices - V : v0, v1, ..., v(V-1). Also apply mapping:  to
    every edge -> a positive real number(weight) - initially empty."""

    def __init__(self, v_in):
        """constructor -  takes number of vertices and creates a graph
         with no edges (E = 0) and an empty adjacent lists of vertices"""
        self.V = v_in
        _array = [x for x in zip(range(v_in), [False] * v_in)]
        self.V_array = []
        for x in _array:
            self.V_array.append(list(x))
        self.E = 0
        self.adj = []
        for i in range(v_in):
            self.adj.append([])

    def V(self):
        """returns number of vertices"""
        return self.V

    def E(self):
        """returns number of edges"""
        return self.E

    def weight(self, v, w):
        """Takes an edge - two vertices and returns an associated to it weight"""
        return self.adj[v][w - 1][1]

    def add_edge(self, v, w, c):
        """adds an edge to the graph, takes two integers (two vertices: v, w), a cost c
         and creates an edge v,w - by modifying appropriate adjacent lists of heaps which
         contains pairs: vertex, weight [those heaps]"""
        self.adj[v].append([w, c])
        self.adj[w].append([v, c])
        self.E += 1

    def adj_list(self, v):
        """Takes an integer - a graph vertex and returns the adjacency lists of it"""
        return self.adj[v]

    def mark(self, v):
        self.V_array[v][1] = True

    def is_marked(self, v):
        if self.V_array[v][1] is True:
            return True
        else:
            return False

    def __str__(self):
        """to string method, prints the graph"""
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + " "
            s += "\n"
        return s

class DirectedGraph:
    """Class graph, creates a graph - described by integers - number
    of vertices - V : v0, v1, ..., v(V-1)"""

    def __init__(self, v_in):
        """constructor -  takes number of vertices and creates a graph
         with no edges (E = 0) and an empty adjacent lists of vertices"""
        self.V = v_in
        _array = [x for x in zip(range(v_in), [False] * v_in)]
        self.V_array = []
        for x in _array:
            self.V_array.append(list(x))
        self.E = 0
        self.adj = []
        for i in range(v_in):
            self.adj.append([])

    def V(self):
        """returns number of vertices"""
        return self.V

    def E(self):
        """returns number of edges"""
        return self.E

    def add_edge(self, v, w):
        """adds an edge to the graph, takes two integers (two vertices)
         and creates an edge v,w - by modifying appropriate adjacent lists """
        self.adj[v].append(w)
        self.E += 1

    def adj_list(self, v):
        """Takes an integer - a graph vertex and returns the adjacency lists of it"""
        return self.adj[v]

    def mark(self, v):
        self.V_array[v][1] = True

    def is_marked(self, v):
        if self.V_array[v][1] is True:
            return True
        else:
            return False

    def __str__(self):
        """to string method, prints the graph"""
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + " "
            s += "\n"
        return s


