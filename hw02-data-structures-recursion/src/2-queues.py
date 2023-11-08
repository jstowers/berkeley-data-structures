#!/usr/bin/env python
# coding: utf-8

# #### queues

# In[ ]:


from dsa.Queue import Queue


# In[ ]:


q = Queue()
q.enqueue(10)
print(q.peek())
print(q)


# In[ ]:


print(q.dequeue())
print(q.is_empty())
print(q.peek())


# In[ ]:


print(q)


# example with names

# In[ ]:


q.enqueue("Alex")
q.enqueue("Beth")
q.enqueue("Chris")
q.enqueue("Dinh")


# In[ ]:


q


# In[ ]:


q.dequeue()


# In[ ]:


q.dequeue()


# In[ ]:


q


# In[ ]:


q.enqueue("Eva")


# In[ ]:


q


# In[ ]:


q.dequeue()


# In[ ]:


q


# In[ ]:


q.dequeue()
q.dequeue()
q


# example with numbers

# In[ ]:


for i in range(10):
    q.enqueue(i)
print(q)


# In[ ]:


while not q.is_empty():
    print(q.dequeue())


# In[ ]:


q


# In[ ]:


q.dequeue()


# In[ ]:





# In[ ]:


for i in range(11):
    q.enqueue(i)
print(q)


# In[ ]:


q


# In[ ]:


q.dequeue()


# In[ ]:


q


# In[ ]:


q.dequeue()


# In[ ]:


q


# In[ ]:


q.enqueue(10)


# In[ ]:


q.enqueue(11)


# In[ ]:


q.enqueue(12)


# In[ ]:


q


# In[ ]:


while not q.is_empty():
    print(q.dequeue())


# #### queue overflow

# In[ ]:


q = Queue()
for i in range(100):
    q.enqueue(i)
print(q)


# #### dynamic queue

# In[ ]:


from dsa.Queue import DynamicQueue
dq = DynamicQueue()
for i in range(100):
    dq.enqueue(i)
print(dq)


# In[ ]:


while not dq.is_empty():
    print(dq.dequeue())
print(dq)

