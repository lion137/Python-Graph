# Simple data structure: bag, needed for afs.


class Bag:
    def __init__(self):
        self.data = []

    def __add__(self, other):
        self.data.append(other)

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def pick(self):
        if not self.is_empty():
            tmp = self.data[-1]
            self.data.pop(-1)
            return tmp

    def print_bag(self):
        print(self.data)


