# Graph - undirected implemented with adjacency matrix
class AdjacencyMatrixGraph:
    def __init__(self, labels):
        self.labels = labels
        self.node_count = len(self.labels)
        self.matrix = self.__create_matrix()
        self.label_index = self.__create_label_table()

    # create 2D matrix where each vertex has a row and column
    def __create_matrix(self):
        rows, cols = [self.node_count, self.node_count]
        return [[None for i in range(cols)] for j in range(rows)]
    
    # create hash table of { label : index }
    def __create_label_table(self):
        ht = {}

        # enumerate returns a tuple: (index, value)
        for i, label in enumerate(self.labels):
            ht.update({label:i})

        print("ht =", ht)
        return ht

    # add undirected edge to graph
    def add_edge(self, start_label, end_label):
        
        # get integer index for each vertex
        start = self.label_index[start_label]
        end = self.label_index[end_label]

        # define undirected edge
        self.matrix[start][end] = True
        self.matrix[end][start] = True
        self.matrix[start][start] = True
        self.matrix[end][end] = True

    def dfs(self, start, end):

        # run depth-first recursion
        return self.depth_first_recursion(start, end)
    
    def check_graph_index(self, label):

        if self.label_index.get(label) is None:
            return None

        elif self.label_index.get(label) >= 0:
            return self.label_index.get(label)
        
        return None
        
    # Depth_first_recursion receives a start label and end label and
    # recursively traverses the graph searching for the end vertex.
    #
    # If the end vertex is found, the function returns a path array [] showing the 
    # path taken. If the end vertex is not found, the function returns None.
    def depth_first_recursion(self, start_label, end_label, visited = None, path = None):
        
        # check graph for start vertex
        start_index = self.check_graph_index(start_label)
        if start_index is None:
            print("start vertex", start_label, "does not exist in graph.")
            return None

        # check graph for end vertex
        end_index = self.check_graph_index(end_label)
        if end_index is None:
            print("end vertex", end_label, "does not exist in graph.")
            return None

        # initialize visited hash table
        # { index : True } for each visited vertex 
        if visited is None:
            visited = {}

        # initialize path array
        if path is None:
            path = []

        # add current vertex to visited hash table
        visited[start_index] = True

        # add label to path
        path.append(start_label)

        # recursion base case
        if start_index == end_index:
            return path

        # loop through adjacent vertices
        for i in range(len(self.matrix)):
            #print("start_index = ", start_index, " i =", i)
            #print("self.matrix[start_index][i] =", self.matrix[start_index][i])
            if i not in visited and self.matrix[start_index][i]:
                #print("self.labels[i] =", self.labels[i])
                path.append(self.labels[i])
                return self.depth_first_recursion(self.labels[i], end_label, visited, path)

        return None

    # print graph in matrix form
    def print_graph(self):
        print()
        print("   |", end="")
        for label in self.labels:
            print(f"{label:^3}", end=" ")
        print()
        print("----" * (len(self.matrix) + 1))
        for r, row in enumerate(self.matrix):
            label = self.labels[r]
            print(f"{label:^3}|", end="");
            for col in row:
                b = " T " if col else "   "
                print(b, end=" ")
            print()
