# Course Schedule II

## Problem

Return order of courses given prerequisites.

If impossible, return empty.


## Idea

Use DFS Topological Sort.
Detect cycle using recursion stack.


## Algorithm

1. Build graph
2. DFS each node
3. Detect cycle
4. Add to order
5. Reverse order


## Complexity

Time: O(V + E)

Space: O(V + E)


## Code

See solution.py