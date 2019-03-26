class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = list()
        self.searched = False
        self.parent = None

    def add_edge(self, nhb):
        self.edges.append(nhb)
        nhb.edges.append(self)
