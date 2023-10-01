# HW 4
# Problem No. 2

# Union of Two Linked Lists
# --------------------------
# Write a function that takes two linked list and outputs a union of these 
# two linked lists. Make it as efficient as possible. You can assume that 
# each list consists of unique numbers and are not necessarily sorted. 
# Also, the order of the output is not significant.

# Example
# ---------
# [ 2, 10, 5, 3, 4] and [ 4, 7, 8, 3, 11 ] has a union of [ 2, 10, 3, 4, 5, 7, 8, 11 ]

from dsa.LinkedList import LinkedList

# CreateUnion receives two linked lists and returns a 
# new linked list representing a union of the two lists.
def createUnion(link1, link2):

    union = LinkedList()
    ht = {}

    updateUnion(union, ht, link1)
    updateUnion(union, ht, link2)

    return union

# UpdateUnion receives a union set, a hash table to 
# track values, and a link_list.  It updates the
# hash table and union set if a value from the
# link_list is unique to the union set.
def updateUnion(union, ht, link_list):
    curr = link_list.head

    while curr is not None:
        value = curr.value
        count = ht.get(value)

        # if value not in ht,
        # add to ht and union
        if count is None:
            ht.update({value:1})
            union.append(value)
        else:
            ht.update({value:count+1})

        curr = curr.next

# define Test class and instantiate test cases
class Test:
    def __init__(self, list1 = None, list2 = None):
        self.list1 = list1
        self.list2 = list2
        self.link_list1 = LinkedList()
        self.link_list1.from_array(self.list1)
        self.link_list2 = LinkedList()
        self.link_list2.from_array(self.list2)

test1 = Test([2, 10, 5, 3, 4], [4, 7, 8, 3, 11])
test2 = Test([29, 23, 19, 17, 13, 11, 7], [2, 3, 5, 7, 11])

# define and execute test suite
test_suite = [
    test1,
    test2
]

for index, test in enumerate(test_suite):
    union = createUnion(test.link_list1, test.link_list2)
    print(f'{index + 1}. link1 = {test.link_list1}') 
    print(f'   link2 = {test.link_list2}')
    print(f'   union = {union}')
    print("--------------------------------------------------------------")