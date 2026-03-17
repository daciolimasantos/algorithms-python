# Number of Connected Components

## Problem

Count connected components in an undirected graph.


## Idea

Use Union Find.

Each node starts as its own parent.

Union nodes when an edge exists.


## Algorithm

initialize union find

for each edge
union nodes

count remaining components


## Complexity

Time: O(E * α(N))

Space: O(N)


## Code

See solution.py