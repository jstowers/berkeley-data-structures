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

class BinaryTree:
    def __init__(self, node=None, count=0):
        self.root = node
        self.count = count
    
    def from_array(self, list=None):
        if list is None:
            return
        
        for element in list:
            self.insert(element)
    
    def insert(self, value):
        current = self.root

        if self.root is None:
            self.root = Node(value)
            self.count += 1
            return
        
        # values inserted first on left side
        # then on the right side
        while current is not None:
            if current.left is None:
                current.left = Node(value)
                self.count += 1
                return
            else:
                if current.right is None:
                    current.right = Node(value)
                    self.count += 1
                    return
        
            # alternate current to balance tree
            if (self.count%2 == 0):
                current = current.left
            else:
                current = current.right
        
        return

    def print(self):
        self.root.print()