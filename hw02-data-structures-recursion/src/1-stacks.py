#!/usr/bin/env python
# coding: utf-8

# #### static stack demo

# In[ ]:


from dsa.Stack import Stack


# In[ ]:


st = Stack()

st.push("new document")
print(st.peek())
print(st)




# In[ ]:


st.pop()


# In[ ]:


st.peek()


# In[ ]:


st


# In[ ]:


st.push("new document")
st.push("copy document")
st.push("rename document")
st.push("delete document")


# In[ ]:


while not st.is_empty():
    print(st.pop())


# In[ ]:





# #### push then pop

# In[ ]:


for n in range(10):
    st.push(n)
    print(st.peek())
print(st)


# In[ ]:


while not st.is_empty():
    print(st.pop())


# #### overflow demo

# In[ ]:


for n in range(10):
    st.push(n)
    print(st.peek())
print(st)


# In[ ]:


st.push(11)


# #### dynamic stack demo

# In[ ]:


from dsa.Stack import DynamicStack

ds = DynamicStack()
ds.push(10)
print(st.peek())
print(st)


# In[ ]:





# In[ ]:


for n in range(100):
    ds.push(n)
    print(ds.peek())
print(ds)


# In[ ]:




