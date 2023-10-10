# HW 5
# Problem No. 2

# Min Heap Sort
# --------------------
# Write a heap sort function.  Implement heap sort as a min
# heap to sort an array in ascending order.  Try implementing
# it without looking at the source code for max heap.

from MinHeap import MinHeap

# min heap #1
mh = MinHeap()
mh.insert(50)
mh.insert(40)
mh.insert(30)
mh.insert(20)
mh.insert(10)
mh.insert(15)
mh.insert(17)
mh.insert(12)

# print min heap
mh.print()
print()

# sort min heap
sorted1 = mh.sort()
print("sorted1 =", sorted1)

print("\n------------------------------")

# min heap #2
minheap = MinHeap()

for i in [49, 9, 36, 16, 81, 64, 25]:
    minheap.insert(i)

# print min heap
minheap.print()
print()

# sort min heap
sorted2 = minheap.sort()
print("sorted2 =", sorted2)

