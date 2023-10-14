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

        # enumerate returns a tuple (index, value)
        for i, label in enumerate(self.labels):
            ht.update({label:i})

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

        # define path array
        path = self.depth_first_recursion(start, end, {}, [])

        return path

    def depth_first_recursion(self, start_label, end_label, visited, path):

        # start vertex
        start_index = self.label_index[start_label]
        print("start_index =", start_index)

        # end vertex
        end_index = self.label_index[end_label]

        # add current vertex to visited hash table
        visited[start_index] = True
        print("visited =", visited)
  



        if start_index == end_index:
            print("inside IF")
            return path

        # loop through adjacent vertices
        for i in range(len(self.matrix)):
            print(self.matrix[start_index][i])
            if i not in visited and self.matrix[start_index][i]:
                path.append(self.labels[i])
                print("path =", path)
                return self.depth_first_recursion(self.labels[i], end_label, visited, path)



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


class Vertex:
    def __init__(self, value):
        self.value = value
        self.ad
    