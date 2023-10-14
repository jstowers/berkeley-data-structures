# __Graph Depth First Traversal__

## Overview

1. visit all vertices in a graph using depth-first traversal

2. traversal occurs vertically, then horizontally

3. uses a stack or recursion


## Creating an Undirected Graph

An undirected graph will use an __adjacency matrix__.  This is a two-dimensional array where each vertex has a corresponding row and column.  The vertex itself, and its adjacent vertices,
are marked with an `x`.

  A ------- B ------- C
   \         \       /
    \         \     /
     \         \   /
      \         \ /
       D -- E -- F

        A   B   C   D   E   F
    A   x   x       x
    B   x   x   x           x
    C       x   x           x
    D   x           x   x
    E               x   x   x
    F       x   x       x   x

    The matrix is symmetrical along the downward diagnoal from [A,A] to [F, F].


## DFS Algorithm

1. start at a given vertex

2. add current vertex to visited hash table

3. process vertex

4. iterate through current vertex's adjacent vertices

    a.  if adjacent vertex has already been visited, ignore it

    b.  otherwise, recursively perform traversal on adjacent vertex

