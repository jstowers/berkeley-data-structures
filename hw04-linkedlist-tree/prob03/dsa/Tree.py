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

# Binary Search Tree (BST)
class Tree:
    def __init__(self, node=None):
        self.root = node
        
    def search(self, value):
        current = self.root
        
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return False
        
        return False
    
    def insert(self, value):

        current = self.root

        if self.root is None:
            self.root = Node(value)
            return
        
        while current is not None:
            if value <= current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                else:
                    current = current.right
            else:
                return 
        
        return
   
    def delete_node(self, value, node=None):
        if node is None:
            node = self.root
        
        if value < node.value:
            node.left = self.delete_node(value, node.left)
        elif value > node.value:
            node.right = self.delete_node(value, node.right)
        else:
            if node.left is None:
                branch = node.right
                node = None
                return branch
            elif node.right is None:
                branch = node.left
                node = None
                return branch
            
            branch = self.min_node(node.right)
            node.value = branch.value
            node.right = self.delete_node(branch.value, node.right)
            
        return node

    def min_node(self, node=None):
        if node is None:
            node = self.root
        
        if node.left is None:
            return node
        else:
            return self.min_node(node.left)
    
    def min_value(self):
        return self.min_node().value
    
    def max_node(self, node=None):
        if node is None:
            node = self.root
        
        if node.right is None:
            return node
        else:
            return self.max_node(node.right)
    
    def max_value(self):
        return self.max_node().value
    
    def print(self):
        self.root.print()

    # public method to sum all node values
    def sum(self):
        return self.__sum_in_order(self.root, 0)
    
    # private method with depth first traversal
    def __sum_in_order(self, node, total):
        if node is not None:
            total = self.__sum_in_order(node.left, total)
            total += node.value
            total = self.__sum_in_order(node.right, total)
        return total


