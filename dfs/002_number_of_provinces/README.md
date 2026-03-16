# Number of Provinces

## Problem

Given adjacency matrix of cities,
find number of connected provinces.


## Idea

Each province is a connected component.

Use DFS to visit all connected nodes.


## Algorithm

1. Loop nodes
2. If not visited
3. DFS
4. Count province


## Complexity

Time: O(n^2)

Space: O(n)


## Code

See solution.py