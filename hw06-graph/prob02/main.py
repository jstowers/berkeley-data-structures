# HW 6
# Problem No. 2

# Graph - Breadth First Search
# ----------------------------
# Implement a breadth first search function that accepts a starting
# vertex and an ending vertex of a graph. Assume that the graph is 
# implemented using an adjacency matrix.

from Graph import AdjacencyMatrixGraph

# graph labels
labels = ["A", "B", "C", "D", "E", "F"]

# initialize directed graph
dgraph = AdjacencyMatrixGraph(labels)

# define directed edges: from -> to
dgraph.add_directed_edge("A", "B")
dgraph.add_directed_edge("A", "D")

dgraph.add_directed_edge("B", "C")
dgraph.add_directed_edge("B", "F")

dgraph.add_directed_edge("C", "D")
dgraph.add_directed_edge("C", "F")

dgraph.add_directed_edge("D", "E")
dgraph.add_directed_edge("E", "F")

dgraph.print_graph()
print()

path1 = dgraph.bfs("A", "C")
print("A -> C path =", path1)
print()