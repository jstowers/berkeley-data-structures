#!/usr/bin/env python
# coding: utf-8

# In[1]:


import deque

dq = deque.Deque()


# In[ ]:


# peek empty
print(dq.peek_left())


# In[ ]:


print(dq.peek_right())


# In[ ]:


# test one element


# In[ ]:


dq = deque.Deque()
dq.append_left(1)
print(dq.peek_left())
print(dq.peek_right())


# In[ ]:


dq = deque.Deque()
dq.append_right(1)
print(dq.peek_left())
print(dq.peek_right())


# #### append left, pop left - stack behavior

# In[ ]:


dq = deque.Deque()
for i in range(10):
    dq.append_left(i)

while not dq.is_empty():
    print(dq.pop_left())


# #### append right, pop right - stack behavior

# In[ ]:


dq = deque.Deque()
for i in range(10):
    dq.append_right(i)

while not dq.is_empty():
    print(dq.pop_right())


# #### append left, pop right - queue behavior

# In[ ]:


dq = deque.Deque()
for i in range(10):
    dq.append_left(i)

while not dq.is_empty():
    print(dq.pop_right())


# #### append right, pop left - queue behavior

# In[ ]:


dq = deque.Deque()
for i in range(10):
    dq.append_right(i)

while not dq.is_empty():
    print(dq.pop_left())


# In[ ]:




