# Diameter of Binary Tree

## Problem

Return the diameter of a binary tree.

Diameter = longest path between two nodes.


## Idea

Use DFS to compute height.
Update diameter using left + right.


## Algorithm

1. DFS node
2. Get left height
3. Get right height
4. Update diameter
5. Return height


## Complexity

Time: O(n)

Space: O(n)


## Code

See solution.py