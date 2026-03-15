# Rotting Oranges

## Problem

You are given a grid where:

0 = empty
1 = fresh orange
2 = rotten orange

Each minute, rotten oranges infect neighbors.

Return the number of minutes until all are rotten.


## Idea

Use BFS starting from all rotten oranges.

Spread rot level by level.


## Algorithm

1. Add all rotten oranges to queue
2. Count fresh oranges
3. BFS level by level
4. Decrease fresh count
5. Count minutes


## Complexity

Time: O(m * n)

Space: O(m * n)


## Code

See solution.py
