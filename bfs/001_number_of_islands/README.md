# Number of Islands

## Problem

Given a 2D grid of "1" (land) and "0" (water),
count the number of islands.

An island is surrounded by water.


## Idea

Use BFS to explore all connected land cells.
Every time we find a new land cell,
we start a BFS and mark the whole island.


## Algorithm

1. Iterate over grid
2. When find "1"
3. Run BFS
4. Mark visited as "0"
5. Count islands


## Complexity

Time: O(m * n)

Space: O(m * n)


## Code

See solution.py
