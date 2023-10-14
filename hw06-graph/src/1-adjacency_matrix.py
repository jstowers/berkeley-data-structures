#!/usr/bin/env python
# coding: utf-8

# Adjacency Matrix - undirected graph

# In[1]:


from dsa.Graphs import AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph


# <div>
# <img src="images/Slide5.png" name="Directed Graph" width="500"/>
# </div>
# 

# In[ ]:


labels = ["A", "B", "C", "D", "E", "F"]
graph = AdjacencyMatrixGraph(labels)
graph.print_graph()


# In[ ]:


graph.add_adjacent_vertex("A", "B") 
graph.add_adjacent_vertex("A", "D")

graph.add_adjacent_vertex("B", "C")
graph.add_adjacent_vertex("B", "F")

graph.add_adjacent_vertex("C", "D")
graph.add_adjacent_vertex("C", "F")

graph.add_adjacent_vertex("D", "E")
graph.add_adjacent_vertex("E", "F")


# In[ ]:


graph.print_graph()


# Directed Graph

# <div>
# <img src="images/Slide6.png" alt="Directed Graph" width="500"/>
# </div>
# 

# In[ ]:


labels = ["A", "B", "C", "D", "E", "F"]
dgraph = AdjacencyMatrixGraph(labels)
dgraph.print_graph()


# In[ ]:


dgraph.add_adjacent_directed_vertex("A", "B") 
dgraph.add_adjacent_directed_vertex("A", "D")

dgraph.add_adjacent_directed_vertex("B", "C")
dgraph.add_adjacent_directed_vertex("B", "F")

dgraph.add_adjacent_directed_vertex("C", "D")
dgraph.add_adjacent_directed_vertex("C", "F")

dgraph.add_adjacent_directed_vertex("D", "E")
dgraph.add_adjacent_directed_vertex("E", "F")



dgraph.print_graph()


# Weighted Graph (Directed)

# <div>
# <img src="images/Slide6.png" alt="Weighted Directed Graph", width="500"/>
# </div>
# 

# In[ ]:


labels = ["A", "B", "C", "D", "E", "F"]

wgraph = AdjacencyMatrixWeightedGraph(labels)

wgraph.add_adjacent_directed_vertex("A", "B", 3) # A -> B: weight 3
wgraph.add_adjacent_directed_vertex("A", "D", 2) # A -> D: weight 2

wgraph.add_adjacent_directed_vertex("B", "C", 5) # B -> C: weight 5
wgraph.add_adjacent_directed_vertex("B", "F", 2) # B -> F: weight 2

wgraph.add_adjacent_directed_vertex("C", "D", 1)  # C -> D: weight 1
wgraph.add_adjacent_directed_vertex("C", "F", 10) # C -> F: weight 10

wgraph.add_adjacent_directed_vertex("D", "E", 6) # D -> E: weight 6
wgraph.add_adjacent_directed_vertex("E", "F", 3) # E -> F: weight 3
wgraph.print_graph()


# In[ ]:




