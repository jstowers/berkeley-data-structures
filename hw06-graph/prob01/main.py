# HW 6
# Problem No. 1

# Graph - Depth First Search
# --------------------------
# Write a depth first search function that accepts a starting vertex 
# and an ending vertex. If the ending vertex is found, It should also 
# return the path of the search.

from Graph import AdjacencyMatrixGraph


def dfs(start, end):

    # define path array
    path = []




    # if end is found, return path
    last_index = len(path) - 1
    if(path[last_index] == end):
        return path
    else:
        return None
    

# graph01
# define undirected graph using adjacency matrix
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

g = AdjacencyMatrixGraph(labels)
g.print_graph()

g.add_edge("A", "B")

g.print_graph()


