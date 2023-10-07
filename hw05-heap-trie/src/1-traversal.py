#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from dsa.Tree import Node, Tree
from dsa.Queue import Queue

n = Node(40)
n.left = Node(20)
n.left.left = Node(10)
n.left.right = Node(30)

n.right = Node(60)
n.right.left = Node(50)
n.right.right = Node(70)

t = Tree(n)
t.print()


# #### Preorder: traverse parents first, starting from the left (parent, left, right)

# In[ ]:


def preorder(node):
    if not node:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)
    
preorder(t.root)


# #### searching for values

# In[ ]:


def search_tree(node, target):
    if not node:
        return None
    elif node.value == target:
        return target
    else:
        return search_tree(node.left, target) or search_tree(node.right, target)

search_tree(t.root, 100)


# In[ ]:


search_tree(t.root, 50)


# #### Inorder: left, parent then right

# ###### used for building a sorted list

# In[ ]:


def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)

inorder(t.root)


# #### Postorder: traverse leaves first (left, right, parent)

# In[ ]:


def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)

postorder(t.root)


# #### tree height example

# In[ ]:


def tree_height(node, height=0):
    if not node:
        return height
    return max(tree_height(node.left, height + 1), tree_height(node.right, height + 1))

tree_height(t.root)


# In[ ]:


t.root.right.right.right = Node(80)


# In[ ]:


tree_height(t.root)


# #### Level Order (Breadth First Search)

# #### print/process elements by level order

# In[ ]:


def level_order(node):
    queue = Queue()
    queue.enqueue(node)

    while not queue.is_empty():
        current = queue.dequeue()
        print(current.value)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)

level_order(t.root)


# In[ ]:




