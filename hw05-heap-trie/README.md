

## Priority Queue

The classic example is a hospital's emergency triage system.
A patient with a life-threatening injury is placed in front of the
queue even if he arrives after a patient suffering from the flu.

Priority queue is an __abstract data type__.  It can be implemented
using other, more fundamental data structures.

### Implementation

An __ordered array__ works well for a priority queue.

1. To insert data, we always maintain proper order.

2. To delete data, we always remove from the end of the array.


### Efficiency

1. Insertion - O(n)

You have to check each element to find the correct place.  Then you may have to shift the remaining elements to the right.

2. Deletion - O(1)

You only delete from the end of the array.

Because of insertion's inefficiency, computer scientists developed a new data structure called a __heap__ that performs even better.

---

## Heap

A __binary heap__ is a binary tree that maintains the following conditions:

1. __heap condition__

    a.  max heap - the value of each node must be greater than each of its descendants.

    b.  min heap - the value of each node must be less than each of its descendants.

2. __the tree is complete__



### Heap Condition

#### Max Heap

             100
            /   \
          88     25
         /  \   /  \
       87   16 8   12

Here, the root node `100` is greater than all of its descendants.  The node `88` is greater than its two descendant nodes, 87 and 16.  The node `25` is greater than its two descendant nodes, 8 and 12.

Note the difference between a heap and a binary search tree (BST).  In a BST, the right children of a node are always greater than the node.  This is never the case with a heap.  The children of a heap node are always less than the node.

#### Min Heap

              10 
            /   \
          20     30
         /  \   /  \
       40   50 60  70
      /  \
     80  90

The root node `10` is smaller than all of its descendants.  The same goes for the `20` and `30` nodes.

### Complete Trees

The tree is completely filled with nodes.  On each level, from left to right, all nodes have values.

The bottom row _can_ have empty positions, as long as there are no nodes to the right of an empty position.

Complete:

             O                              
           /   \     
          O     O
         / \   / \
        O   O O   O

             O                              
           /   \     
          O     O
         / \   /
        O   O O

Incomplete:

             O
            / \
           O   O
         /    / \
        O    O   O


### Heap Properties

1. __weakly ordered__ - while heaps have _some_ order, their descendants in a max heap are greater than their ancestor, this doesn't make a heap amenable to searching.

2. __root node__ is the greatest value in a max heap.  The root node is the smallest value in a min heap.


### Alternative Heap Implementations

An array implementation is the most common.

An alternate implementation is to use linked nodes.
