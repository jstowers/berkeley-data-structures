class Deque:
    # initialize new Deque instance with capacity of 10 elements
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.front = -1
        self.count = 0
   
    # insert an element at front
    def append_left(self, element):
        if len(self) >= len(self.array):
            raise Exception("capacity reached")
        self.front = 0
        self.count += 1

        if self.count > 1:
            for i in range(self.count-1, 0, -1):
                temp = self.array[i-1]
                self.array[i] = temp

        self.array[self.front] = element

    # insert an element at back
    def append_right(self, element):
        if len(self) >= len(self.array):
            raise Exception("capacity reached")
        self.front = 0
        self.count += 1
        self.array[self.count - 1] = element

    # remove first element
    def pop_left(self):
        element = self.array[0]
        self.front += 1
        self.count -= 1
        return element
    
    # remove last element
    def pop_right(self):
        if self.is_empty():
            raise Exception("empty deque")
        element = self.array[self.count-1]
        self.count -= 1
        return element

    # examine first element
    def peek_left(self):
        if self.is_empty():
            raise Exception("empty deque")
        return self.array[self.front]

    # examine last element
    def peek_right(self):
        if self.is_empty():
            raise Exception("empty deque")
        return self.array[self.front + self.count - 1]

    # return number of elements
    def get_count(self):
        return self.count

    # print each element
    def print(self):
        for i in range(self.front, len(self), 1):
            print("index #{} = {}".format(i, self.array[i]))

    # check for empty deque
    def is_empty(self):
        return self.count == 0
    
    # length of deque
    def __len__(self):
        return self.count