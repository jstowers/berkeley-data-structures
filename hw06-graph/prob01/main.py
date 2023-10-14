# HW 6
# Problem No. 1

# Graph - Depth First Search
# --------------------------
# Write a depth first search function that accepts a starting vertex 
# and an ending vertex. If the ending vertex is found, It should also 
# return the path of the search.

from Graph import AdjacencyMatrixGraph




# graph01
# define undirected graph using adjacency matrix
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

g = AdjacencyMatrixGraph(labels)
g.print_graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "E")
g.add_edge("C", "F")
g.add_edge("C", "D")
g.add_edge("D", "G")
g.add_edge("E", "F")
g.add_edge("E", "H")
g.add_edge("F", "H")
g.add_edge("F", "I")
g.add_edge("G", "I")

g.print_graph()

path = g.dfs("A", "H")
print("path =", path)
