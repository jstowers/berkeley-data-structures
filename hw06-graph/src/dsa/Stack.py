class Stack:
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.top = -1
    
    def push(self, element):
        if len(self) >= len(self.array):
            raise Exception("Capacity Reached")
        self.top += 1
        self.array[self.top] = element
        
    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        element = self.array[self.top]
        self.top -= 1
        return element
    
    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.array[self.top]
    
    def __len__(self):
        return self.top + 1
    
    def is_empty(self):
        return self.top <= -1

    def __repr__(self):
        return f"{self.array[0:self.top + 1]} Top: {self.top} Capacity: {len(self.array)}"
    
    
class DynamicStack(Stack):
    def grow(self):
        # create new array with new size
        new_array = [ None ] * len(self.array) * 2
        
        # copy elements
        for i, e in enumerate(self.array):
            new_array[i] = e

        self.array = new_array

    def shrink(self):
        # create new array with new size
        if len(self.array) < 10:
            return

        new_size = len(self.array) // 2
        new_array = [ None ] * new_size
        
        # copy elements
        for i in range(new_size):
            new_array[i] = self.array[i]

        self.array = new_array


    def check_capacity(self):
        if self.top + 1 >= len(self.array):
            self.grow()
        elif (self.top + 1) * 4 <= len(self.array):
            self.shrink()
        
    def push(self, element):
        self.check_capacity()
        super().push(element)
        
    def pop(self):
        self.check_capacity()
        return super().pop()

