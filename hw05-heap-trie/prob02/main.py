# HW 5
# Problem No. 2

# Min Heap Sort
# --------------------
# Write a heap sort function.  Implement heap sort as a min
# heap to sort an array in ascending order.  Try implementing
# it without looking at the source code for max heap.


from math import floor, log

class MinHeap:
    def __init__(self):
        self.array = []

    def root_node(self):
        if self.size() == 0:
            return None

        return self.array[0]

    def last_node(self):
        return self.array[self.size()-1]
    
    def size(self):
        return len(self.array)
    
    def parent_index(self, index):
        return floor((index-1)/2)
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def insert(self, value):
        # add new value at end of array
        self.array.append(value)
        
        # determine index of new value
        i_new = self.size() - 1
        print("i_new =", i_new)

        # determine index of parent
        i_parent = self.parent_index(i_new)

        # implement trickle up algorithm
        while (i_new > 0 and self.array[i_new] < self.array[i_parent]):
            # swap new value with parent value
            self.array[i_new], self.array[i_parent] = self.array[i_parent], self.array[i_new]
            
            # set new node index to parent node index
            i_new = i_parent
            
            # determine index of parent
            i_parent = self.parent_index(i_new)

    # supporting print method
    def prepare(self, e, field):
        return str(e).center(field)

    # supporting print method
    def level(self, h):
        return self.array[self.first(h):self.last(h)]

    # supporting print method
    def first(self, h):
        return 2**h - 1
    
    # supporting print method
    def last(self, h):
        return self.first(h+1)

    # print heap in tree form
    def print(self, width = None):
        if width is None:
            width = max(len(str(e)) for e in self.array)
        height = int(log(len(self.array), 2)) + 1
        gap = ' ' * width
        for h in range(height):
            below = 2 ** (height - h -1)
            field = (2 * below -1) * width
            print(gap.join(self.prepare(e, field) for e in self.level(h)))

mh = MinHeap()
mh.insert(50)
mh.print()

mh.insert(40)
mh.print()

mh.insert(30)
mh.print()

mh.insert(20)
mh.print()

mh.insert(10)
mh.print()

mh.insert(15)
mh.print()

mh.insert(17)
mh.print()

mh.insert(12)
mh.print()

root = mh.root_node()
print("first =", root)