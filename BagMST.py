# Bag designed to work with the MST algorithm; essentially a Heap
# with modification.


import heap as hp


class MSTBag:
    """Modified Bag, to pick the cheapest costs for MST
    algorithm; internally maintains a heap"""

    def __init__(self):
        self.__qe = {}
        self.__bag = hp.BinHeap()

    def is_empty(self):
        return not bool(self.__qe)

    def __add__(self, other):
            self.__qe[other[1]] = other[0]
            self.__bag.insert(other[1])

    def pop(self):
            tmp = self.__bag.del_min()
            tmp0 = [self.__qe.get(tmp), tmp]
            self.__qe.__delitem__(tmp)
            return tmp0

    def __str__(self):
        s = "["
        s += str(self.__qe)
        s += "]"
        return s





