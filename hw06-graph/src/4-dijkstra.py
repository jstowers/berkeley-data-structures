#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dsa.Graphs import WeightedGraphVertex


# In[ ]:


def shortest_path(start, end):
    weight_table = {}
    previous = {}
    visited = {}
    queue = [] # ideally, a min heap
    
    current = start
    queue.append(current)
    weight_table[current.value] = 0
    previous[current.value] = current
    
    while len(queue) > 0:
        current_weight = weight_table.get(current.value, None)
        visited[current.value] = True

        # assume a weight of 1 for non-weighted version
        for adjacent in current.adjacent_vertices:
            if isinstance(current.adjacent_vertices, dict): # hack
                weight = current.adjacent_vertices[adjacent]
            else:
                weight = 1
            if not visited.get(adjacent.value, False):
                queue.append(adjacent)

            wt = weight_table.get(adjacent.value, None)
            if not wt or wt > weight + current_weight:
                print(weight_table)
                weight_table[adjacent.value] = weight + current_weight
                previous[adjacent.value] = current

        current = queue[0]
        del queue[0]
            
    return weight_table, previous

def find_path(start, end):
    weight_table, previous = shortest_path(start, end)
    path = []

    current = end
    path.append(current.value)
    while current != start:
        current = previous[current.value]
        path.append(current.value)
        
    path.reverse()
    print("Weight Table")
    print(weight_table)
    print("Previous Vertex Table")
    print(previous)
    print("Distance ", weight_table[end.value])
    return path



# <div>
# <img src="images/Slide7.png" alt="Weighted Directed Graph" width="500"/>
# </div>
# 

# In[ ]:


a = WeightedGraphVertex("a")
b = WeightedGraphVertex("b")
c = WeightedGraphVertex("c")
d = WeightedGraphVertex("d")
e = WeightedGraphVertex("e")
f = WeightedGraphVertex("f")

a.add_directed_adjacent_vertex(b, 3)
a.add_directed_adjacent_vertex(d, 4)
a.add_directed_adjacent_vertex(f, 20)

b.add_directed_adjacent_vertex(c, 4)
c.add_directed_adjacent_vertex(f, 5)
d.add_directed_adjacent_vertex(e, 5)

e.add_directed_adjacent_vertex(b, 2)
e.add_directed_adjacent_vertex(f, 2)


# In[ ]:


find_path(a, f)


# undirected version gives different results

# <div>
# <img src="images/Slide9.png" alt="Weighted Undirected Graph" width="500"/>
# </div>
# 

# In[ ]:


a = WeightedGraphVertex("a")
b = WeightedGraphVertex("b")
c = WeightedGraphVertex("c")
d = WeightedGraphVertex("d")
e = WeightedGraphVertex("e")
f = WeightedGraphVertex("f")

a.add_adjacent_vertex(b, 3)
a.add_adjacent_vertex(d, 4)
a.add_adjacent_vertex(f, 20)

b.add_adjacent_vertex(c, 4)
c.add_adjacent_vertex(f, 5)
d.add_adjacent_vertex(e, 5)

e.add_adjacent_vertex(b, 2)
e.add_adjacent_vertex(f, 2)


# In[ ]:


find_path(a, f)


# non-weighted version = BFS

# In[2]:


from dsa.Graphs import Vertex
a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")
f = Vertex("f")

a.add_adjacent_vertex(b)
a.add_adjacent_vertex(d)
a.add_adjacent_vertex(f)

b.add_adjacent_vertex(c)
c.add_adjacent_vertex(f)
d.add_adjacent_vertex(e)

e.add_adjacent_vertex(b)
e.add_adjacent_vertex(f)


# In[ ]:


find_path(a, f)


# ![title](traversal_example/Slide3.png)
# 

# In[ ]:


af = WeightedGraphVertex("Africa")
asia = WeightedGraphVertex("Asia")
au = WeightedGraphVertex("Australia")
eu = WeightedGraphVertex("Europe")
gl = WeightedGraphVertex("Greenland")
na = WeightedGraphVertex("North America")
sa = WeightedGraphVertex("South America")

af.add_adjacent_vertex(eu, 2)
af.add_adjacent_vertex(asia, 2)
af.add_adjacent_vertex(au, 10)
af.add_adjacent_vertex(sa, 2)

asia.add_adjacent_vertex(au, 3)
asia.add_adjacent_vertex(eu, 1)

eu.add_adjacent_vertex(gl, 3)
eu.add_adjacent_vertex(na, 8)

gl.add_adjacent_vertex(na, 2)

na.add_adjacent_vertex(sa, 1)




# North America to Australia

# In[ ]:


find_path(na, au)


# Australia to North America

# In[ ]:


find_path(au, na)


# South America to Asia

# In[ ]:


find_path(sa, asia)


# In[ ]:




