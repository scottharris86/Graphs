"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex)

        #create a set to store the visited verticies
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            vertex = q.dequeue()
            
            # if vertex has not been visited
            if vertex not in visited: 
                # mark the vertex as visited
                visited.add(vertex)
                # print it for debug for now
                print(vertex)

                # add all of its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(vertex):
                    q.enqueue(next_vertex)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push a starting vertex
        s = Stack()
        s.push(starting_vertex)

        #create a set to store the visited verticies
        visited = set()

        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            vertex = s.pop()
            
            # if vertex has not been visited
            if vertex not in visited: 
                # mark the vertex as visited
                visited.add(vertex)
                # print it for debug for now
                print(vertex)

                # add all of its neighbors to the top of the stack
                for next_vertex in self.get_neighbors(vertex):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)
        for value in self.vertices[starting_vertex]:
            if value not in visited:
                self.dft_recursive(value, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create and empty queue and enqueue PATH to starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        
        # created a set to store visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            vertex = path[-1]

            # check if the vertex has not been visited
            if vertex not in visited:
                # is this the vertex the target?
                if vertex == destination_vertex:
                    # return the path
                    return path

                # mark as vistited
                visited.add(vertex)

                # then add a path to its neighbors to the back of the queue


                # make a copy of the path
                
                
                # append the neighbor to the back of the path
                for new_vertex in self.get_neighbors(vertex):
                    new_path = path.copy()
                    new_path.append(new_vertex)
                # enqueue new path
                    q.enqueue(new_path)

        # return None
        return None
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create and empty Stack and push PATH to starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        
        # created a set to store visited vertices
        visited = set()

        # while the stack is not empty
        while s.size() > 0:
            # dequeue the first path
            path = s.pop()
            # grab the last vertex from the path
            vertex = path[-1]

            # check if the vertex has not been visited
            if vertex not in visited:
                # is this the vertex the target?
                if vertex == destination_vertex:
                    # return the path
                    return path

                # mark as vistited
                visited.add(vertex)

                # then add a path to its neighbors to the back of the queue


                # make a copy of the path
                
                
                # append the neighbor to the back of the path
                for new_vertex in self.get_neighbors(vertex):
                    new_path = path.copy()
                    new_path.append(new_vertex)
                # enqueue new path
                    s.push(new_path)

        # return None
        return None
        

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = [starting_vertex]
        
        if starting_vertex == destination_vertex:
            # print(path)
            return path

        for new_vertex in self.vertices[starting_vertex]:
            if new_vertex not in path:   
                new_path = path.copy()
                new_path.append(new_vertex)
                # print(new_path)
                value = self.dfs_recursive(new_vertex, destination_vertex, new_path)
                if value is not None:
                    return value


        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
