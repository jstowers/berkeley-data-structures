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
print()

path5 = g.dfs("A", "D")
print("A -> D path =", path5)
print()

path1 = g.dfs("A", "I")
print("A -> I path =", path1)
print()

path6 = g.dfs("A", "H")
print("A -> H path =", path6)
print()

# different starting vertex
path3 = g.dfs("F", "B")
print("F -> B path =", path3)
print()

# None - "X" does not exist
path2 = g.dfs("A", "X")
print("A -> X path =", path2)
print()

# None - "Y" does not exist
path4 = g.dfs("Y", "B")
print("Y -> B path =", path4)
print()


# graph02
labels2 = ["A", "B", "C", "D", "E", "F"]

g2 = AdjacencyMatrixGraph(labels2)

g2.add_edge("A", "B")
g2.add_edge("A", "D")
g2.add_edge("B", "C")
g2.add_edge("B", "F")
g2.add_edge("C", "D")
g2.add_edge("C", "F")
g2.add_edge("D", "A")
g2.add_edge("D", "E")
g2.add_edge("E", "F")

g2.print_graph()

g2_path1 = g2.dfs("A", "B")
print("A -> B path =", g2_path1)
print()

g2_path2 = g2.dfs("A", "F")
print("A -> F path =", g2_path2)
print()

g2_path3 = g2.dfs("D", "B")
print("D -> B path =", g2_path3)
print()


# graph03
labels3 = ["A", "B", "C", "D"]

g3 = AdjacencyMatrixGraph(labels3)

g3.add_edge("A", "B")
g3.add_edge("B", "C")
g3.add_edge("B", "D")

g3.print_graph()

g3_path1 = g3.dfs("A", "B")
print("A -> B path =", g3_path1)
print()

g3_path2 = g2.dfs("A", "C")
print("A -> C path =", g3_path2)
print()

g3_path3 = g2.dfs("A", "D")
print("A -> D path =", g3_path3)
print()