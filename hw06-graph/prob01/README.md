# __Graph Depth First Traversal__

## Overview

1. visit all vertices in a graph using depth-frist traversal

2. traversal occurs vertically, then horizontally

3. uses a stack or recursion


## Algorithm

1. start at a given vertex

2. add current vertex to visited hash table

3. process vertex

4. iterate through current vertex's adjacent vertices

    a.  if adjacent vertex has already been visited, ignore it

    b.  otherwise, recursively perform traversal on adjacent vertex

