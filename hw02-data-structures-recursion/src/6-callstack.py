#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(5)


# #### call stack limitation

# In[ ]:


factorial(10_000)


# In[ ]:


import sys
sys.getrecursionlimit()


# In[ ]:


factorial(1000)


# In[ ]:




