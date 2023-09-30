# HW 4
# Problem No. 1

# Reverse Doubly Linked List
# --------------------------
# Write a function to reverse the elements in a doubly linked list. 
# Do not simply print it out. It must have the references correctly set in reversed order.
# Also, write a print method – this should help with debugging.

from dsa.DoublyLinkedList import Node, DoublyLinkedList

# create using array method
array = [10, 20, 30, 40, 50]
dll = DoublyLinkedList()
dll.from_array(array)

# ReverseDoublyLinkedList receives a doubly linked list and returns 
# the list with each element's previous and next pointer references 
# reversed and the head and tail pointer references updated.
def reverseDoublyLinkedList(dll):

    print("===== before =====")
    dll.print()
    print()

    # set current node
    curr = dll.head
  
    while curr is not None:
        prev = curr.prev
       
        # set tail
        if prev is None:
            dll.tail = curr

        # reverse elements
        next = curr.next
        curr.prev = next
        curr.next = prev

        # set head
        if next is None:
            dll.head = curr

        # increment current node
        curr = next

    print("===== after =====")
    dll.print()
    return dll

result = reverseDoublyLinkedList(dll)
print("result =", result)