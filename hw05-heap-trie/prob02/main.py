# HW 5
# Problem No. 2

# Min Heap Sort
# --------------------
# Write a heap sort function.  Implement heap sort as a min
# heap to sort an array in ascending order.  Try implementing
# it without looking at the source code for max heap.

from MinHeap import MinHeap

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

while mh.size() > 0:
    print(mh.delete())

print("\n------------------------------\n")

minheap = MinHeap()

for i in [49, 9, 36, 16, 81, 64, 25]:
    minheap.insert(i)

minheap.print()

while minheap.size() > 0:
    print(minheap.delete())
