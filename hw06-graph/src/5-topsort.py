#!/usr/bin/env python
# coding: utf-8

# ### Topological Sort

# Topological Sort Functions

# In[1]:


from dsa.Graphs import Vertex

def count_in_degree(graph):
    in_degree = {}
    queue = []
    
    queue.append(graph)
    in_degree[graph] = 0
    
    while len(queue) > 0:
        current = queue[0]
        del queue[0]
        for adjacent in current.adjacent_vertices:
            if adjacent not in in_degree:
                in_degree[adjacent] = 1
            else:
                in_degree[adjacent] += 1
            if adjacent not in queue:
                queue.append(adjacent)
            
    for v, indeg in in_degree.items():
        print(v.value, indeg)
        
    return in_degree

def insert_queue(in_degree, queue):
    ''' enqueue any vertex with in-degree of 0 to the queue '''
    for vertex, in_degrees in in_degree.items():
        if in_degrees == 0:
            queue.append(vertex)

def top_sort(graph):
    in_degree = count_in_degree(graph)
    
    queue = []
    ordering = []

    insert_queue(in_degree, queue)
    while len(queue) > 0:
        current = queue[0]
        del queue[0]
        
        if current.value not in ordering:
            ordering.append(current.value)
            
        for adjacent in current.adjacent_vertices:
            if in_degree[adjacent] > 0:
                in_degree[adjacent] -= 1
                if in_degree[adjacent] == 0:
                    queue.append(adjacent)
    return ordering


# <div>
# <img src="images/Slide10.png" alt="DAG" width="500"/>
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


a.add_directed_adjacent_vertex(b)
a.add_directed_adjacent_vertex(c)
a.add_directed_adjacent_vertex(d)

b.add_directed_adjacent_vertex(e)
c.add_directed_adjacent_vertex(e)

d.add_directed_adjacent_vertex(f)

e.add_directed_adjacent_vertex(g)
f.add_directed_adjacent_vertex(g)

top_sort(a)


# In[ ]:





# In[ ]:




