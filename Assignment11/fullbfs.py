from bestgraph import Graph

# From Lab13
class Queue:
    """
    Code created by Kurt Zimmer
    """
    
    def __init__(self):
        """
        Initializes the queue with a data structure such as a list
        or an array
        """
        self.lst = []

    def size(self):
        """
        Gets the size of the queue
        """
        return len(self.lst)
    
    def isEmpty(self):
        """
        Checks to see if the queue is empty. 
        Returns: True if empty
                 False otherwise
        """
        return len(self.lst) == 0
    
    def dequeue(self):
        """
        Removes an item from the front of the queue and 
        returns it. 
        This implementation checks to make sure the queue is 
        not empty. 
        """
        if not self.isEmpty():
            return self.lst.pop(0)
        else:
            return None
    
    def enqueue(self, item):
        """
        Adds an item to the back of the queue
        """
        self.lst.append(item)
    
    def __str__(self):
        return str(self.lst)

def bfsfull(g,node):
    q = Queue()
    q.enqueue(node)

    u = {i for i in g.nodes}
    v = set()

    while not q.isEmpty():
        xnode = q.dequeue()
        if not xnode in v:
            v.add(xnode)
            print(xnode)
            for i in g.children(xnode):
                q.enqueue(i)
    
    for i in u-v:
        q.enqueue(i)
        while not q.isEmpty():
            xnode = q.dequeue()
            if not xnode in v:
                v.add(xnode)
                print(xnode)
                for i in g.children(xnode):
                    q.enqueue(i)
                
    pass

if __name__ == "__main__":
    my_graph = Graph([1,2,3,4,5,6,7,8])
    elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,4),(6,7)]

    for i in elst:
        my_graph.add_edge(i)
    print(my_graph.edges)
    bfsfull(my_graph,5)