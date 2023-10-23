# __Graph Breadth First Traversal__

## Overview

1. visit all vertices in a graph using breadth-first traversal

2. traversal occurs horizontally, then vertically

3. uses a queue

## BFS Algorithm 

1. start at a given vertex

2. add current vertex to queue

3. add current vertex to visited hash table

4. while queue is not empty

    a. dequeue current vertex

    b. process current vertex

    c. for all _unvisited_ adjacent vertices of the current vertex:

        i. enqueue unvisted adjacent vertex

        ii. add unvisted adjacent vertex to hash table
