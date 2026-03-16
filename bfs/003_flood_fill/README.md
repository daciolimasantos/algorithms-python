# Flood Fill

## Problem

Given an image represented by a grid,
replace the color of the starting pixel
and all connected pixels with the same color.


## Idea

Use BFS to visit all connected cells
with the same original color.


## Algorithm

1. Save original color
2. Start BFS from (sr, sc)
3. Visit neighbors
4. Change color
5. Continue until done


## Complexity

Time: O(m * n)

Space: O(m * n)


## Code

See solution.py