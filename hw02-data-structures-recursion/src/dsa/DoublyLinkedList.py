class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, head=None, tail=None, count=0):
        self.head = head
        self.tail = tail
        self.count = count

    def from_array(self, mylist=None):
        self.head = None
        self.tail = None
        self.count = 0

        if mylist is None:
            return

        # append each from given list
        for element in mylist:
            self.append(element)
        
    def __repr__(self):
        s = "[ "
        current = self.head
        while current is not None:
            s += str(current.value) + " "
            current = current.next

        return f"{s}] Count: {self.count}"
    
    def reverse(self):
        current = self.tail
        while current is not None:
            print(current.value, end=" ")
            current = current.prev
        print()

    def search(self, value):
        i = 0
        current = self.head
        while current is not None:
            if current.value == value:
                return i
            i += 1
            current = current.next
        raise Exception("Value not found")
    
    def insert(self, index, value):
        ''' need to check for index out of bounds '''
        i = 0
        
        # insert front
        if index == 0:
            self.prepend(value)
            return
            
        current = self.head
        while index < i or current is not None:
            if i == index:
                break
            current = current.next
            i += 1

        if index > i:
            raise Exception("Index Out of Bounds")
        new_node = Node(value)
        
        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node
        new_node.prev.next = new_node

        self.count += 1

        
    def prepend(self, value):
        ''' prepend value at the beginning of the list '''
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.count += 1

    def append(self, value):
        ''' append value to the end of the list '''
        
        if self.head is None:
            self.head = Node(value)
            if self.count == 0:
                self.tail = self.head
            self.count += 1
            return
        
        # go to the end of the list
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

        self.count += 1
        

    def delete(self, index):
        if self.head is None:
            raise Exception("DoublyLinkedList is Empty")

        i = 0
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return
        
        current = self.head
        while current is not None:
            if index == i:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.count -= 1
                return
            current = current.next
            i += 1
        raise Exception("Index not found")

