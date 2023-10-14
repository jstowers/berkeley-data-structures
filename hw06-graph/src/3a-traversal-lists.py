#!/usr/bin/env python
# coding: utf-8

# Adjacency List Implementation

# In[ ]:


from dsa.Graphs import Vertex


# Undirected Graph

# <div>
# <img src="images/Slide1.png" alt="Undirected Graph" width="500"/>
# </div>
# 

# In[ ]:


a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
g = Vertex("G")
h = Vertex("H")
i = Vertex("I")

a.add_adjacent_vertex(b)
a.add_adjacent_vertex(c)
a.add_adjacent_vertex(d)

b.add_adjacent_vertex(e)

c.add_adjacent_vertex(d)
c.add_adjacent_vertex(f)

d.add_adjacent_vertex(g)

e.add_adjacent_vertex(f)
e.add_adjacent_vertex(h)

f.add_adjacent_vertex(i)
g.add_adjacent_vertex(i)

h.add_adjacent_vertex(f)


# depth first traversal

# In[ ]:


a.df_traverse()


# depth first search

# From A to C (Goes through E and F)

# In[ ]:


a.dfs(c)


# From A to I (skipped H)

# In[ ]:


a.dfs(i)


# breadth first traversal

# In[ ]:


a.bf_traverse()


# breadth first search

# From A to C (Goes to B also)

# In[ ]:


a.bfs(c)


# From A to I (Goes through all vertices)

# In[ ]:


a.bfs(i)


# #### Directed Graph

# <div>
# <img src="images/Slide2.png" alt="Directed Graph" width="500"/>
# </div>
# 

# In[ ]:


a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
g = Vertex("G")
h = Vertex("H")
i = Vertex("I")

a.add_directed_adjacent_vertex(b)
a.add_directed_adjacent_vertex(c)
a.add_directed_adjacent_vertex(d)

b.add_directed_adjacent_vertex(e)

c.add_directed_adjacent_vertex(d)
c.add_directed_adjacent_vertex(f)

d.add_directed_adjacent_vertex(g)

e.add_directed_adjacent_vertex(h)

f.add_directed_adjacent_vertex(e)
f.add_directed_adjacent_vertex(h)
f.add_directed_adjacent_vertex(i)

g.add_directed_adjacent_vertex(i)



# Depth first traversal on a directed graph

# In[ ]:


a.df_traverse()


# Breadth first traversal on a directed graph

# In[ ]:


a.bf_traverse()


# In[ ]:




