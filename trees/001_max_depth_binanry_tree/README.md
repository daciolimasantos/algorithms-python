# Max Depth of Binary Tree

## Problem

Return the maximum depth of a binary tree.


## Idea

Use DFS recursion.
Depth = 1 + max(left, right)


## Algorithm

1. If null return 0
2. DFS left
3. DFS right
4. Return max + 1


## Complexity

Time: O(n)

Space: O(n)


## Code

See solution.py