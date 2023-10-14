# Graph - undirected implemented with adjacency matrix
class AdjacencyMatrixGraph:
    def __init__(self, labels):
        self.labels = labels
        self.node_count = len(self.labels)
        self.array = self.__create_matrix()
        self.label_index = self.__create_lable_table()

    # create 2D matrix where each vertex has a row and column
    def __create_matrix(self):
        rows, cols = [self.node_count, self.node_count]
        return [[None for i in range(cols)] for j in range(rows)]
    
    # create hash table of { label : index }
    def __create_lable_table(self):
        ht = {}

        # enumerate returns a tuple (index, value)
        for i, label in enumerate(self.labels):
            ht.update({label:i})

        return ht 
    
    # returns the index of the label from the labels array
    def __get_label_index(self, label):
        return self.labels.index(label)

    # add undirected edge to graph
    def add_edge(self, start_label, end_label):
        
        # get integer index for each vertex
        start = self.label_index[start_label]
        end = self.label_index[end_label]

        # define undirected edge
        self.array[start][end] = True
        self.array[end][start] = True
        self.array[start][start] = True
        self.array[end][end] = True


    # print graph in matrix form
    def print_graph(self):
        print()
        print("   |", end="")
        for label in self.labels:
            print(f"{label:^3}", end=" ")
        print()
        print("----" * (len(self.array) + 1))
        for r, row in enumerate(self.array):
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
    