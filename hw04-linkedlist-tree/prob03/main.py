# HW 4
# Problem No. 3


# Binary Search Tree (BST) Operations
# -----------------------------------
# Write the following binary search tree functions to:
# 1. Return the minimum value
# 2. Return the maximum value
# 3. Return the sum of all values

from dsa.Tree import Tree
from dsa.sorttools import rand_int_array

# initialize a random array of integers
array = rand_int_array(20, 118)
#array = [7, 19, 24, 27, 35, 22, 15, 19, 29, 35, 21, 26, 28, 30, 5, 3, 6]
print("array =", array)

# min value
min = min(array)
print("min =", min)

# max value
max = max(array)
print("max =", max)

# sum of all values
sum = sum(array)
print("sum =", sum)

# initialize BST and populate with array elements
tree = Tree()
for i, e in enumerate(array):
    tree.insert(e)

tree.print()

# find minimum value
min_value = tree.min_value()
print("min_value =", min_value)

# find maximum value
max_value = tree.max_value()
print("max_value =", max_value)

# find sum of all values
tree_sum = tree.sum()
print("tree_sum =", tree_sum)
