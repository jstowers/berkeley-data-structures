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

