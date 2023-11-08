#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(10)


# In[3]:


def factorial_tail(n, prod=1):
    if n <= 1:
        return prod
    return factorial_tail(n - 1, n * prod)
    
factorial_tail(10)


# In[4]:


def mysum(array):
    if len(array) == 0:
        return 0
    return array[0] + mysum(array[1:])
mysum([1, 2, 3, 4])


# In[5]:


def mysum_tail(array, total=0):
    if len(array) == 0:
        return total
    return mysum_tail(array[1:], array[0] + total)
mysum_tail([1, 2, 3, 4])


# In[7]:


def search(array, target, i=0):
    if i >= len(array):
        return -1

    if array[i] == target:
        return i
    else:
        return search(array, target, i + 1)

print(search([10, 20, 30, 40], 30))
print(search([10, 20, 30, 40], 0))


# Fibonacci Series

# Each number in the fibonacci series is the sum of the previous two

# 
# F(n) = F(n - 1) + F(n - 2)
# 

# |n|0| 1|2 |3 |4 |5| 6| 7|8|9|
# |-|-|-|-|-|--|--|--|--|--|--|
# |F(n)|0|1|1|2| 3| 5| 8| 13|21|34|
# 
# 

# Iterative Version

# In[ ]:


def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        tmp = a
        a = a + b
        b = tmp
    return a


# print the first 10 numbers of the Fibonacci series

# In[ ]:


for n in range(10):
    print(n, "\t", fib_iter(n))    


# Benchmark For Iterative Fibonacci

# In[ ]:


get_ipython().run_cell_magic('time', '', 'fib_iter(40)\n')


# Naive Recursive Fibonacci

# In[ ]:


def fib_rec(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    return fib_rec(n - 1) + fib_rec(n - 2)


# print the first 10 numbers of the Fibonacci series

# In[ ]:


for n in range(10):
    print(n, "\t", fib_rec(n))


# Benchmark

# In[ ]:


get_ipython().run_cell_magic('time', '', 'fib_rec(33)\n')


# Tail Recursive Version of Fibonacci

# In[ ]:


def fib_tail(n, a=1, b=0):
    if n == 1:
        return a
    elif n <= 0:
        return b
    return fib_tail(n - 1, a + b, a)


# In[ ]:


for n in range(10):
    print(n, "\t", fib_tail(n))


# Benchmark

# In[ ]:


get_ipython().run_line_magic('time', '')
fib_tail(40)


# In[ ]:




