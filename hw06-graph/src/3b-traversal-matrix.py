#!/usr/bin/env python
# coding: utf-8

# Adjacency Matrix Implementation

# In[1]:


from dsa.Graphs import AdjacencyMatrixGraph


# Undirected Graph

# <div>
# <img src="images/Slide1.png" alt="Undirected Graph" width="500"/>
# </div>
# 

# In[ ]:


graph = AdjacencyMatrixGraph(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
graph.print_graph()


# In[ ]:


graph.add_adjacent_vertex("A", "B")
graph.add_adjacent_vertex("A", "C")
graph.add_adjacent_vertex("A", "D")

graph.add_adjacent_vertex("B", "E")

graph.add_adjacent_vertex("C", "D")
graph.add_adjacent_vertex("C", "F")

graph.add_adjacent_vertex("D", "G")

graph.add_adjacent_vertex("E", "F")
graph.add_adjacent_vertex("E", "H")

graph.add_adjacent_vertex("F", "I")
graph.add_adjacent_vertex("G", "I")

graph.add_adjacent_vertex("H", "F")

graph.print_graph()


# depth first traversal

# In[ ]:


graph.df_traverse("A")


# breadth first traversal

# In[ ]:


graph.bf_traverse("A")


# #### Directed Graph

# <div>
# <img src="images/Slide2.png" alt="Directed Graph" width="500"/>
# </div>
# 

# In[ ]:


graph = AdjacencyMatrixGraph(["A", "B", "C", "D", "E", "F", "G", "H", "I"])

graph.add_adjacent_directed_vertex("A", "B")
graph.add_adjacent_directed_vertex("A", "C")
graph.add_adjacent_directed_vertex("A", "D")

graph.add_adjacent_directed_vertex("B", "E")

graph.add_adjacent_directed_vertex("C", "D")
graph.add_adjacent_directed_vertex("C", "F")

graph.add_adjacent_directed_vertex("D", "G")

graph.add_adjacent_directed_vertex("E", "H")

graph.add_adjacent_directed_vertex("F", "E")
graph.add_adjacent_directed_vertex("F", "H")
graph.add_adjacent_directed_vertex("F", "I")

graph.add_adjacent_directed_vertex("G", "I")

graph.print_graph()


# Depth first traversal on a directed graph

# In[ ]:


graph.df_traverse("A")


# Breadth first traversal on a directed graph

# In[ ]:


graph.bf_traverse("A")


# In[ ]:




