import numpy as np

class Edge:
    def __init__(self, a = 0, b = 0, w = 0.0):
        """
        Initialize an edge in a graph
        
        param:
            a : a vertex of the edge
            b : the other vertex of the dge
            w : the weight of the edge
        """
        self.a = a
        self.b = b
        self.w = w
    
class Vertex:
    def __init__(self, weights:np.ndarray):
        """
           Define a vertex with all the edges connected to it.

        param:
            weights : a array of all the weights of all the edges coonected to it. 
        """
        self.w = weights.copy()


class universe:
    """
        Graph Cut 
    """

    def __init__(self, num_edges, num_vertices):
        self.vertices = [Vertex(np.zeros(6,)) for i in range(num_vertices)]
        
    