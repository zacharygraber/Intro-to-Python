class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self, pair):
        start,end = pair
        if (not start in self.nodes) or (not end in self.nodes):
            return -1
        elif end in self.edges[start]:
            return -1
        else:
            self.edges[start].append(end)
            return 1
    
    def add_node(self, n):
        if n in self.nodes:
            return -1
        else:
            self.nodes.append(n)
            self.edges[n] = []
            return 1
    
    def del_node(self, n):
        if not n in self.nodes:
            return -1
        else:
            self.nodes.remove(n)
            self.edges = {i:self.edges[i] for i in self.edges if i != n}
            return 1
    
    def children(self,node):
        return self.edges[node]
    
    def nodes(self):
        return str(self.nodes)
    
    def __str__(self):
        return str(self.edges)