# Depth First Search implemented as a function.
# Data structure used as a bag is LIFO stack, implemented in compiler
# via recursion. Of course when exceed stack capacity, we can use stack explicitly,
# like in the other versions


def dfs(g, v):
    if g.is_marked(v) is False:
        g.mark(v)
        for w in g.adj_list(v):
            dfs(g, w)

            
