class Graph:
    """
    Graph Representation of class
    Created by Dr. D
    Modified by AIs
    """
    def __init__(self, nodes, directed):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
        self.directed = directed
    
    def add_edge(self, pair):
        """
        Adds an edge between the first node to 
        the second node in the list
        """
        start, end = pair
        self.edges[start].append(end)
        if not self.directed:
            self.edges[end].append(start)
    
    def children(self, node):
        """
        Returns a list of all nodes attached to the node provided
        """
        if node in self.nodes:
            return self.edges[node]
        else:
            return []
    
    def dettachedNodes(self):
        """
        Returns a list of nodes have no edges
        """
        if not self.directed:
            return [i for i in self.nodes if not self.edges[i]]
        else:
            return [i for i in self.nodes if (not self.edges[i] or not [j for j in self.edges if i in self.edges[j]])]
        # CHALLENGE: Can you make it for a directional graph to return nodes that have no edges COMING IN and leaving
    
    def __str__(self):
        finalString = ""
        for n in self.nodes:
            finalString += str(n) + " -> " + str(self.edges[n]) + "\n"
        return finalString
