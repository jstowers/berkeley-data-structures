# HW 5
# Problem No. 2

# Min Heap Sort
# --------------------
# Write a heap sort function.  Implement heap sort as a min
# heap to sort an array in ascending order.  Try implementing
# it without looking at the source code for max heap.


from math import floor, log

from src.dsa.Heap import Heap

class MinHeap:
    def __init__(self):
        self.array = []

    def root(self):
        if self.size() == 0:
            return None

        return self.array[0]

    def last(self):
        if self.size() == 0:
            return None

        return self.array[self.size()-1]
    
    def size(self):
        return len(self.array)
    
    def parent_index(self, index):
        return floor((index-1)/2)
    
    def has_left_child(self, index):
        return self.left_child_index(index) < self.size()
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def has_right_child(self, index):
        return self.right_child_index(index) < self.size()

    def right_child_index(self, index):
        return (index * 2) + 2
    
    # add new value to heap
    def insert(self, value):
        # add new value at end of array
        self.array.append(value)
        
        # index of new value
        i_new = self.size() - 1

        # heapify up
        self.swim(i_new)

    # heapify up
    def swim(self, i):

        # determine index of parent
        i_parent = self.parent_index(i)

        # restore heap condition
        while (i > 0 and self.array[i] < self.array[i_parent]):
            # swap new value with parent value
            self.array[i], self.array[i_parent] = self.array[i_parent], self.array[i]
            
            # set new node index to parent node index
            i = i_parent
            
            # determine index of parent
            i_parent = self.parent_index(i)


    # return heap in sorted order
    def delete(self):
        root = self.root()

        start_index = 0

        # delete root value and replace with last
        if self.size() == 1:
            self.array.pop()
        else:
            self.array[start_index] = self.array.pop()

        self.sink(start_index)

        return root
    
    # heapify down
    def sink(self, index):
        
        while self.has_lesser_child(index):

            # find lesser child index
            smaller_child_index = self.calculate_smaller_child_index(index)

            # swap trickle node with its smaller child:
            self.array[smaller_child_index], self.array[index] = self.array[index], self.array[smaller_child_index]

            # update index
            index = smaller_child_index

    # check whether node at index has left and right 
    # children and if any of the children are less than
    # the node value at the index
    def has_lesser_child(self,index):

        return ((self.has_left_child(index) and 
            self.array[self.left_child_index(index)] < self.array[index])
            or (self.has_right_child(index) and
                self.array[self.right_child_index(index)] < self.array[index]))
    
    def calculate_smaller_child_index(self, index):

        # if no right child, return left child index
        if self.has_right_child(index) is False:
            return self.left_child_index(index)
        
        # if right child < left child, return right child index
        if self.array[self.right_child_index(index)] < self.array[self.left_child_index(index)]:
            return self.right_child_index(index)
        
        # else, left child < right child, return left child index
        else:
            return self.left_child_index(index)

    # supporting print method
    def prepare(self, e, field):
        return str(e).center(field)

    # supporting print method
    def level(self, h):
        return self.array[self.first_level(h):self.last_level(h)]

    # supporting print method
    def first_level(self, h):
        return 2**h - 1
    
    # supporting print method
    def last_level(self, h):
        return self.first_level(h+1)

    # print heap in tree form
    def print(self, width = None):
        if width is None:
            width = max(len(str(e)) for e in self.array)
        height = int(log(len(self.array), 2)) + 1
        gap = ' ' * width
        print()
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


print("\n------------------------------\n")

minheap = MinHeap()

for i in [49, 9, 36, 16, 81, 64, 25]:
    minheap.insert(i)

minheap.print()

while minheap.size() > 0:
    print(minheap.delete())
