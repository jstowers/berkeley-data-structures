#!/usr/bin/env python
# coding: utf-8

# #### any iterative algorithm can be written recursively

# In[ ]:


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

factorial(5)


# In[ ]:


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(5)


# #### sum

# In[ ]:


def mysum(array):
    total = 0
    for n in array:
        total += n
    return total

mysum([1, 2, 3, 10])


# In[ ]:


def mysum(array):
    if len(array) == 0:
        return 0
    return array[0] + mysum(array[1:])

mysum([1, 2, 3, 10])


# #### search

# In[ ]:


def search(array, target, i=0):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
search([1, 2, 3, 4, 5], 7)


# In[ ]:


def search(array, target, i=0):
    if i >= len(array):
        return -1

    if array[i] == target:
        return i
    else:
        return search(array, target, i + 1)

print(search([10, 20, 30, 40, 50], 50))
print(search([10, 20, 30, 40, 50], 100))


# In[ ]:


def search(array, target, i=0):
    if len(array) == 0:
        return -1

    if array[0] == target:
        return i
    else:
        return search(array[1:], target, i + 1)

print(search([10, 20, 30, 40, 50], 50))
print(search([10, 20, 30, 40, 50], 100))


# In[ ]:




