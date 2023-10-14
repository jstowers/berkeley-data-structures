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


class Queue:
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.front = 0
        self.count = 0
    
    def enqueue(self, element):
        if self.count >= len(self.array):
            raise Exception("Capacity Reached")

        index = (self.front + self.count) % len(self.array)
        self.array[index] = element
        self.count += 1
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")

        element = self.array[self.front]
        self.front += 1
        if self.front >= len(self.array):
            self.front = 0
        self.count -= 1
        return element
    
    def peek(self):
        if self.is_empty():
            raise Exception("Empty Queue")

        return self.array[self.front]

    def is_empty(self):
        return self.count == 0
    
    def __repr__(self):
        arr = []
        for i in range(self.count):
            index = (i + self.front) % len(self.array)
            arr.append(str(self.array[index]))
        arrstr = ", ".join(arr)
        return f"[{arrstr}] Front: {self.front} count: {self.count} Capacity: {len(self.array)}"
    

# shrink not implemented
class DynamicQueue(Queue):
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.front = 0
        self.count = 0
    
    def grow(self):
        # create new array with new size
        new_array = [ None ] * len(self.array) * 2
        
        # copy elements
        for i in range(self.count):
            new_array[i] = self.array[i + self.front]
        self.front = 0
        self.array = new_array

    def check_capacity(self):
        if self.front + self.count >= len(self.array):
            self.grow()

    def enqueue(self, element):
        self.check_capacity()
        index = self.front + self.count
        self.array[index] = element
        self.count += 1


class Array:
    def __init__(self, contents=None, capacity=10):
        ''' contents are optional list/array to fill the array '''
        self.array = [ None ] * capacity
        self.count = 0

        if contents:
            self.extend(contents)
        
    def append(self, element):
        self.array[self.count] = element
        self.count += 1

    def extend(self, array):
        ''' append each element from a given array '''
        for e in array:
            self.append(e)

    def insert(self, index, element):
        if index >= self.count or index < 0:
            raise IndexError

        self.shift_right(self.count, index)
        self.array[index] = element
        self.count += 1
        
    def shift_right(self, start, end):
        for i in range(start, end, -1):
            self.array[i] = self.array[i - 1]

    def delete(self, index):
        if index >= self.count or index < 0:
            raise IndexError

        self.shift_left(index, self.count)
        self.count -= 1

    def shift_left(self, start, end):
        for i in range(start, end):
            self.array[i] = self.array[i + 1]

    ### special methods for handling index operator
    def __getitem__(self, index):
        return self.array[index]
            
    def __setitem__(self, index, value):
        self.array[index] = value
        
    ### special methods for len()
    def __len__(self):
        return len(self.array)

    ### override the representation value with the Python interpreter
    def __repr__(self):
        contents = self.array[:self.count]
        return f'{contents} Count: {self.count} Capacity: {len(self.array)}'
    
    
class DynamicArray:
    def __init__(self, contents=None, capacity=10):
        ''' contents are optional list/array to fill the array '''
        self.array = [ None ] * capacity
        self.count = 0

        if contents:
            self.extend(contents)

        
    def grow(self):
        ''' create new array with double capacity '''
        new_size = len(self.array) * 2
        new_array = [ None ] * new_size

        # copy elements
        for i in range(len(self.array)):
            new_array[i] = self.array[i]

        self.array = new_array

    def shrink(self):
        ''' create new array with half capacity '''
        new_size = len(self.array) // 2
        new_array = [ None ] * new_size
        
        # copy elements
        for i in range(new_size):
            new_array[i] = self.array[i]

        self.array = new_array

    def check_capacity(self):
        if self.count >= len(self.array):
            self.grow()
        elif self.count * 4 <= len(self.array):
            self.shrink()

    def append(self, element):
        self.check_capacity()

        self.array[self.count] = element
        self.count += 1

    def extend(self, array):
        ''' append each element from a given array '''
        for e in array:
            self.append(e)

    def insert(self, index, element):
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_right(self.count, index)
        self.array[index] = element
        self.count += 1
        
    def shift_right(self, start, end):
        for i in range(start, end, -1):
            self.array[i] = self.array[i - 1]

    def delete(self, index):
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_left(index, self.count)
        self.count -= 1

    def shift_left(self, start, end):
        for i in range(start, end):
            self.array[i] = self.array[i + 1]
        
    ### special methods for handling index operator
    def __getitem__(self, index):
        return self.array[index]
            
    def __setitem__(self, index, value):
        self.array[index] = value
        
    ### special methods for len()
    def __len__(self):
        return len(self.array)

    ### override the representation value with the Python interpreter
    def __repr__(self):
        contents = self.array[:self.count]
        return f'{contents} Count: {self.count} Capacity: {len(self.array)}'
