class Graph(object):
    def __init__(self):
        self.nodes = list()
        self.graph = dict()
        self.end = None
        self.start = None

    def reset(self):
        for node in self.nodes:
            node.searched = False
            node.parent = None

    def set_start(self, actor):
        self.start = self.graph[actor]
        return self.start

    def set_end(self, actor):
        self.end = self.graph[actor]
        return self.end

    def add_node(self, node):
        self.nodes.append(node)
        title = node.value
        self.graph[title] = node

    def get_node(self, actor):
        if actor in self.graph.keys():
            return self.graph[actor]
        return None
