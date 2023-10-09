# HW 5
# Problem No. 1

# Last Item in Complete Tree
# --------------------------
# Write a function to get the last item in a complete tree.
# This is easy to do if the complete tree were implemented
# using arrays.  How would we do this if the tree was 
# implemented using nodes?

from math import log
from Queue import Queue

# Node class for binary tree
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print(self, level=0):
        if self.right:
            self.right.print(level + 1)
        print("   " * level + str(self.value))
        if self.left:
            self.left.print(level + 1)

class Heap:

    def __init__(self, node=None):
        self.root = node
        self.count = 0
        self.array = []
    
    def last(self):
        if self.size() == 0:
            return None
  
        # BFS
        last = self.level_order()

        return last.value
    
    def size(self):
        return self.count
    
    def level_order(self, node = None):

        if node is None:
            node = self.root

        queue = Queue()
        queue.enqueue(node)

        while not queue.is_empty():
            current = queue.dequeue()
            last = current
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

        return last


    def insert(self, value):
        current = self.root

        if self.root is None:
            self.root = Node(value)
            self.array.append(value)
            self.count += 1
            return
        
        while current is not None:
            if current.left is None:
                current.left = Node(value)
                self.array.append(value)
                self.count += 1
                return
            elif current.right is None:
                current.right = Node(value)
                self.array.append(value)
                self.count += 1
                return
            elif current.left is not None:
                current = current.left
            elif current.right is not None:
                current = current.right
        return
    
    # supporting print method
    def prepare(self, e, field):
        return str(e).center(field)

    # supporting print method
    def level(self, h):
        return self.array[self.first_level(h):self.last_level(h)]

    # supporting print method
    def first_level(self, h):
        return 2**h - 1
    
    # supporting print method
    def last_level(self, h):
        return self.first_level(h+1)

    # print heap in tree form
    def print(self, width = None):
        if width is None:
            width = max(len(str(e)) for e in self.array)
        height = int(log(len(self.array), 2)) + 1
        gap = ' ' * width
        print()
        for h in range(height):
            below = 2 ** (height - h -1)
            field = (2 * below -1) * width
            print(gap.join(self.prepare(e, field) for e in self.level(h)))



h = Heap()
h.insert(10)
h.insert(20)
h.insert(30)
h.insert(40)
h.insert(50)
h.insert(60)
h.insert(70)
h.insert(80)
h.insert(90)

h.print()

last = h.last()
print("last =", h.last())