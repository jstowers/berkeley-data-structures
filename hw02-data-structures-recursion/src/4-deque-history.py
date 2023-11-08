#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import deque

def add_history(history, url, max_size=5):
    if history.count >= max_size:
        print("popped")
        history.pop_right()
    history.append_left(url)

    
history = deque.Deque(5)
print(history)


# In[ ]:


add_history(history, "amazon.com")
print(history)
add_history(history, "berkeley.edu")
print(history)
add_history(history, "www.ca.gov")
print(history)
#print(history)


# In[ ]:


print(history.peek_left())
print(history.peek_right())


# In[ ]:





# In[ ]:


add_history(history, "didi")
print(history)
add_history(history, "ebay.com")
print(history)
add_history(history, "facebook.com")
add_history(history, "google.com")
print(history)
print(history.peek_left())
print(history.peek_right())


# In[ ]:


import collections

def add_history(history, url, max_size=5):
    if len(history) >= max_size:
        history.pop()
    history.appendleft(url)

    
history = collections.deque()
print(history)
add_history(history, "amazon.com")
add_history(history, "berkeley.edu")
add_history(history, "www.ca.gov")
print(history)
add_history(history, "didi")
print(history)
add_history(history, "ebay.com")
print(history)
add_history(history, "facebook.com")
add_history(history, "google.com")
print(history)
print(history[0])
print(history[-1])


# In[ ]:


dq = collections.deque()
dq.append("A")
dq.appendleft("B")
dq.appendleft("C")
print(dq)
print(dq[-1])
print(dq[0])
print(dq.popleft())
print(dq.pop())
print(dq)


# In[ ]:


dq = collections.deque()
dq.appendleft("A")
dq.append("B")
dq.append("C")
print(dq)
print(dq[0])
print(dq[-1])
print(dq.pop())
print(dq.popleft())
print(dq)


# In[ ]:


dq = deque.Deque()
dq.append_right("A")
dq.append_left("B")
dq.append_left("C")
print(dq)
print(dq.peek_right())
print(dq.peek_left())
print(dq.pop_left())
print(dq.pop_right())
print(dq)


# In[ ]:


dq = deque.Deque()
dq.append_left("A")
dq.append_right("B")
dq.append_right("C")
print(dq)
print(dq.peek_left())
print(dq.peek_right())
print(dq.pop_right())
print(dq.pop_left())
print(dq)


# In[ ]:




