from math import log
from Queue import Queue

# Node class for complete tree
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

# Complete Tree class
class CompleteTree:
    def __init__(self, node=None):
        self.root = node
        self.count = 0
        # array is used for printing purposes only
        self.array = []
    
    # Last returns the last value in the complete tree
    def last(self):
        if self.size() == 0:
            return None
  
        # BFS
        last_node = self.level_order()
        return last_node.value
    
    # Size returns the number of nodes in the tree
    def size(self):
        return self.count
    
    # Level_Order conducts a breadth-first traversal
    # of the tree and returns the last node
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

    # Insert adds a node to the complete tree,
    # following the complete tree conditions
    def insert(self, value):
        current = self.root

        if self.root is None:
            self.root = Node(value)
            # array for printing purposes only
            self.array.append(value)
            self.count += 1
            return
        
        while current is not None:
            if current.left is None:
                current.left = Node(value)
                # array for printing purposes only
                self.array.append(value)
                self.count += 1
                return
            elif current.right is None:
                current.right = Node(value)
                # array for printing purposes only
                self.array.append(value)
                self.count += 1
                return
            elif current.left is not None:
                current = current.left
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

    # print tree
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