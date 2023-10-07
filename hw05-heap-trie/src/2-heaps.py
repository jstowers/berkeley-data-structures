#!/usr/bin/env python
# coding: utf-8

# Heap Example

# In[ ]:


from dsa.Heap import Heap
    
h = Heap()
h.insert(10)
h.insert(20)
h.insert(30)
h.insert(40)
h.insert(50)
h.insert(60)
h.insert(70)
h.insert(80)
h.insert(100)
h.print()


# #### pop all of the elements

# In[ ]:


while h.size() > 0:
    print(h.pop())
    


# #### insert elements that are not in order

# In[ ]:


for i in [49, 9, 36, 16, 81, 64, 25]:
    h.insert(i)
    h.print()
    print()


# #### pop all elements again

# In[ ]:


while h.size() > 0:
    print(h.pop())


# In[ ]:


h.insert(90)


# In[ ]:


h.print()


# In[ ]:


h.pop()


# #### minheap vs maxheap

# In[ ]:


from HeapSolution import Heap
maxheap = Heap(ascending=False)


# In[ ]:


for i in [49, 9, 36, 16, 81, 64, 25]:
    maxheap.insert(i)


# In[ ]:


maxheap.print()


# In[ ]:


while maxheap.size() > 0:
    print(maxheap.pop())


# In[ ]:


minheap = Heap()


# In[ ]:


for i in [49, 9, 36, 16, 81, 64, 25]:
    minheap.insert(i)


# In[ ]:


minheap.print()


# In[ ]:


while minheap.size() > 0:
    print(minheap.pop())


# ### Priority Queue Example

# a priority queue is a general abstract data type, while a heap is a specific data structure used to efficiently implement a priority queue. You can implement a priority queue using other data structures as well, but a heap is one of the most common choices due to its efficiency

# The following example is an implementation of a hospital queue system. 
# Patients are classified by the following priorities:
# * P1 - Critical (Life threatening)
# * P2 - Emergency
# * P3 - Urgent
# * P4 - Non-urgent
# 
# Each patient is also issued a ticket number, which is numbered in the order they visit the hospital.
# 
# Hospitals need to treat patients in order of priority, so a priority queue must be used. This is unlike a standard queue, which is FIFO.

# In[ ]:


from HeapSolution import Heap

class TicketPriorityQueue(Heap):
    ticket_number = 0
    TICKET_MAX = 10_000
    
    def __init__(self):
        super().__init__(ascending=True)

    @staticmethod
    def ticket_to_value(priority, number):
        return int(priority) * TicketPriorityQueue.TICKET_MAX + number

    @staticmethod
    def value_to_ticket(value):
        priority, number = divmod(value, TicketPriorityQueue.TICKET_MAX)
        return f"P{priority}-{number}"
        
    def insert(self, priority):
        if len(priority) != 2 or priority[0] != "P":
            raise Exception("Insert requires format of Pnumber, where number is between 1 and 4")
        self.ticket_number += 1
        value = TicketPriorityQueue.ticket_to_value(priority[1], self.ticket_number)
        super().insert(value)
        
        return TicketPriorityQueue.value_to_ticket(value)
        
    def pop(self):
        return TicketPriorityQueue.value_to_ticket(super().pop())

    def peek(self):
        return super().peek()
        
tpq = TicketPriorityQueue()
patients = ["P4", "P3", "P2", "P1", "P4", "P3", "P2", "P3", "P4", "P1"]
for patient in patients:
    ticket = tpq.insert(patient)
    print(ticket)


# order of ticket processing

# In[ ]:


while tpq.peek():
    print(tpq.pop())


# In[ ]:




