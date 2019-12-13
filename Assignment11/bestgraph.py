import numpy as np

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

    def del_edge(self,e: tuple):
        start, end = e
        if not start in self.nodes:
            return -1
        elif not end in self.edges[start]:
            return -1
        else:
            self.edges[start].remove(end)
            return 1

    def reachable(self, pair):
        x,y = pair
        if x in self.nodes and y in self.nodes:
            a = np.zeros((len(self.nodes), len(self.nodes)), dtype=int)
            for i in range(len(a)):
                for j in range(len(a)):
                    if j+1 in self.edges[i+1]:
                        a[i][j] = 1
            
            a = np.dot(a,a) + a
            a = np.dot(a,a) + a
            return bool(a[x-1][y-1])
        else:
            return False
    
    def children(self,node):
        return self.edges[node]
    
    def nodes(self):
        return str(self.nodes)
    
    def __str__(self):
        return str(self.edges)