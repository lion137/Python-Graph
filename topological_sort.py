# topological sort


import graphs_classes as gr
from lifo_stack import Stack


def topological_sorting(g):
    def topological_sort_helper(s, stack):
        g.mark(s)
        for w in g.adj_list(s):
            if g.is_marked(w) is False:
                topological_sort_helper(w, stack)
        stack.push(s)
    stack = Stack()
    for w in range(g.V):
        if g.is_marked(w) is False:
            topological_sort_helper(w, stack)
    return stack

if __name__ == '__main__':

    g1 = gr.DirectedGraph(9)
    g1.add_edge(0, 3)
    g1.add_edge(1, 3)
    g1.add_edge(2, 3)
    g1.add_edge(3, 5)
    g1.add_edge(3, 8)
    g1.add_edge(4, 5)
    g1.add_edge(5, 6)
    g1.add_edge(6, 7)
    g1.add_edge(8, 7)
    print(topological_sorting(g1))


