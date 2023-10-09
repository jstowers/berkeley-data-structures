# HW 5
# Problem No. 1

# Last Item in Complete Tree
# --------------------------
# Write a function to get the last item in a complete tree.
# This is easy to do if the complete tree were implemented
# using arrays.  How would we do this if the tree was 
# implemented using nodes?

from math import log
from CompleteTree import CompleteTree

ct = CompleteTree()
ct.insert(10)
ct.insert(20)
ct.insert(30)
ct.insert(40)
ct.insert(50)
ct.insert(60)
ct.insert(70)
ct.insert(80)
ct.insert(90)
ct.insert(100)
ct.insert(110)
ct.insert(120)
ct.insert(130)
ct.insert(140)
ct.insert(150)
ct.insert(160)

# print complete tree
ct.print()

# total number of nodes
size = ct.size()
print("size =", size)

# last value in tree
last_value = ct.last()
print("last_value =", last_value)