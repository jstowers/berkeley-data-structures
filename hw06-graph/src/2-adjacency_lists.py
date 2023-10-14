#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dsa.Graphs import Vertex


# #### Undirected Graph

# <div>
# <img src="images/Slide5.png" alt="Unirected Graph" width="500"/>
# </div>
# 

# In[ ]:


a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
a.add_adjacent_vertex(b)
a.add_adjacent_vertex(d)

b.add_adjacent_vertex(a)
b.add_adjacent_vertex(c)
b.add_adjacent_vertex(f)

c.add_adjacent_vertex(b)
c.add_adjacent_vertex(d)
c.add_adjacent_vertex(f)

d.add_adjacent_vertex(a)
d.add_adjacent_vertex(c)
d.add_adjacent_vertex(e)

e.add_adjacent_vertex(d)
e.add_adjacent_vertex(f)

f.add_adjacent_vertex(b)
f.add_adjacent_vertex(c)
f.add_adjacent_vertex(e)


# In[ ]:


a.adjacent_vertices


# In[ ]:


b.adjacent_vertices


# In[ ]:


c.adjacent_vertices


# In[ ]:


d.adjacent_vertices


# In[ ]:


e.adjacent_vertices


# In[ ]:


f.adjacent_vertices


# #### Directed Graph

# <div>
# <img src="images/Slide6.png" alt="Directed Graph" width="500"/>
# </div>
# 

# In[ ]:


a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")

a.add_directed_adjacent_vertex(b)
a.add_directed_adjacent_vertex(d)

b.add_directed_adjacent_vertex(c)
b.add_directed_adjacent_vertex(f)

c.add_directed_adjacent_vertex(d)
c.add_directed_adjacent_vertex(f)

d.add_directed_adjacent_vertex(e)

e.add_directed_adjacent_vertex(f)


# In[ ]:


a.adjacent_vertices


# In[ ]:


b.adjacent_vertices


# In[ ]:


c.adjacent_vertices


# In[ ]:


d.adjacent_vertices


# In[ ]:


e.adjacent_vertices


# In[ ]:


f.adjacent_vertices


# #### Weighted Graph

# <div>
# <img src="images/Slide7.png" alt="Weighted Directed Graph" width="500"/>
# </div>
# 

# In[2]:


from dsa.Graphs import WeightedGraphVertex


# In[ ]:


a = WeightedGraphVertex("A")
b = WeightedGraphVertex("B")
c = WeightedGraphVertex("C")
d = WeightedGraphVertex("D")
e = WeightedGraphVertex("E")
f = WeightedGraphVertex("F")

a.add_adjacent_vertex(b, 3)
a.add_adjacent_vertex(d, 2)

b.add_adjacent_vertex(c, 5)
b.add_adjacent_vertex(f, 2)

c.add_adjacent_vertex(d, 1)
c.add_adjacent_vertex(f, 10)

d.add_adjacent_vertex(e, 6)

e.add_adjacent_vertex(f, 3)


# In[ ]:


a.adjacent_vertices


# In[ ]:


b.adjacent_vertices


# In[ ]:


c.adjacent_vertices


# In[ ]:


d.adjacent_vertices


# In[ ]:


e.adjacent_vertices


# In[ ]:


f.adjacent_vertices


# In[ ]:




