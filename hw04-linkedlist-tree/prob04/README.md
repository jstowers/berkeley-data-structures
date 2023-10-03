# Is a Binary Tree a Binary Search Tree (BST)?

HW Problem #4

Sunday, October 1, 2023

## Binary Tree Definition

A binary tree is a non-linear data structure comprised of nodes.  Each node is either represented as a parent or child.  A parent can have 0, 1, or 2 nodes.  The child nodes are called `left` and `right` nodes.


## BST Conditions

A binary search tree (BST) is a binary tree in which the nodes are ordered by the following conditions:

1. No duplicate values
2. Left descendants contain values lower than ancestor nodes
    max(left subtree) < current.value
3. Right descendants contain values greater than ancestor nodes
    min(right subtree) > current.value
