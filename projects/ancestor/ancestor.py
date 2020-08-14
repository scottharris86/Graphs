# from projects.graph.util import Stack, Queue  # These may come in handy

import os
import sys
sys.path.append(f'{os.getcwd()}/projects/graph')
from util import Stack, Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesnt exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


my_graph = Graph()

def earliest_ancestor(ancestors, starting_node):
    
    for item in ancestors:
        my_graph.add_vertex(item[0])
        my_graph.add_vertex(item[1])
        my_graph.add_edge(item[1], item[0])

    found = my_graph.get_neighbors( starting_node)
    my_min = False
    if found:
        my_min = min(found)
    while my_min:
        found = my_graph.get_neighbors(my_min)
        if found:
            my_min = min(found)
        else:
            return my_min
    return -1

def earliest_ancestor2(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    q = Queue()
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)
            for neighbor in graph.vertices[v]:
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return earliest_ancestor

    
        


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
resp = earliest_ancestor2(test_ancestors, 6)
print(resp)

# self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
# self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
# self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
# self.assertEqual(earliest_ancestor(test_ancestors, 4), -1)
# self.assertEqual(earliest_ancestor(test_ancestors, 5), 4)
# self.assertEqual(earliest_ancestor(test_ancestors, 6), 10)
# self.assertEqual(earliest_ancestor(test_ancestors, 7), 4)
# self.assertEqual(earliest_ancestor(test_ancestors, 8), 4)
# self.assertEqual(earliest_ancestor(test_ancestors, 9), 4)
# self.assertEqual(earliest_ancestor(test_ancestors, 10), -1)
# self.assertEqual(earliest_ancestor(test_ancestors, 11), -1)