# HW 4
# Problem No. 4


# Is Binary Tree a BST?
# ---------------------
# Write a function that accepts a binary tree and verifies whether 
# it fulfills binary search tree conditions.

# BST Conditions
#
# 1. No duplicate values
# 2. Left descendants contain values lower than ancestor nodes
# 3. Right descendants contain values greater than ancestor nodes

from dsa.BinaryTree import BinaryTree, Node

INT_MAX = 4294967296
INT_MIN = -4294967296

def is_tree_BST(tree):
    return is_BST_util(tree.root, INT_MIN, INT_MAX)

def is_BST_util(node, min, max):

    if node is None:
        return True
    
    if node.value < min or node.value > max:
        return False
    
    return (is_BST_util(node.left, min, node.value - 1) and
            is_BST_util(node.right, node.value+1, max))

# define Test class and instantiate test cases
class Test:
    def __init__(self, list = None):
        self.list = list
        self.tree = BinaryTree()
        self.tree.from_array(self.list)

test1 = Test([2, 10, 4]) #false
test2 = Test([4, 2, 10]) #true
test3 = Test([10, 2, 4]) #false
test4 = Test([10, 2, 15]) #true
test5 = Test([10, 8, 15, 6, 9]) #false
test6 = Test([10, 8, 15, 12, 5]) #true
test7 = Test([15, 7, 20, 17, 2, 23, 12, 21]) #true

# define and execute test suite
test_suite = [
    test1,
    test2,
    test3,
    test4,
    test5,
    test6,
    test7
]

for index, test in enumerate(test_suite):
    result = is_tree_BST(test.tree)
    print(test.tree.print())
    print(f'{index + 1}. is tree a BST = {result}') 
    print("--------------------------------------------------------------")