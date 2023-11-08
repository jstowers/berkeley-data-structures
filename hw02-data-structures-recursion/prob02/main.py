# Joseph Stowers
# HW #2
# Tuesday, September 19, 2023


# Fully implement a Deque (double-ended queue) data structure using a static or dynamic array.
# Do not use built-in methods except for the index operator.
# Do not write a wrapper around the built-in Deque class.

from dsa.Deque import Deque


# peek empty
# print(dq.peek_left())


# test one element
# dq = Deque()
#dq.append_right(1)
#dq.append_right(2)
#print(dq.peek_left())
#print(dq.peek_right())
#dq.print()

# append left, pop right - LIFO - stack behavior
dq = Deque()
dq.append_left(1)
dq.append_left(2)
dq.append_left(3)
dq.append_right(4)
dq.append_left(5)
dq.pop_left()
print("peek_left =", dq.peek_left())
print("peek_right =", dq.peek_right())
print("count =", dq.get_count())
dq.print()


# pop right
dq.pop_right()
dq.print()

#while not dq.is_empty():
#    print(dq.pop_right())

# append right, pop left - FIFO - queue behavior
dq = Deque()
for i in range(10):
   dq.append_left(i)
dq.print()

# dq = Deque()
# dq.append_left(1)
# dq.append_left(6)
