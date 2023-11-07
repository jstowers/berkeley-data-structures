class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
        self.head = Node(mylist[0])
        node = self.head
        self.count = 1
        
        for i in mylist[1:]:
            node.next = Node(i)
            node = node.next
            self.count += 1
        self.tail = node
        
            
    def __repr__(self):
        s = "[ "
        current = self.head
        while current is not None:
            s += str(current.value) + " "
            current = current.next

        return f"{s}] Count: {self.count}"
    
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
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return
            
        current = self.head
        while index < i or current is not None:
            i += 1
            if i == index:
                break
            current = current.next
        
        if index > i:
            raise Exception("Index Out of Bounds")
        new_node = Node(value)
        tmp = current.next
        current.next = new_node
        new_node.next = tmp
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
        i = 0
        if index == 0:
            if self.head is None:
                raise Exception("LinkedList is Empty")
            self.head = self.head.next
            self.count -= 1
            return
       
        current = self.head
        prev = current
        while current is not None:
            if index == i:
                prev.next = current.next
                self.count -= 1
                return
            i += 1
            prev = current
            current = current.next
        raise Exception("Index not found")
        
    
