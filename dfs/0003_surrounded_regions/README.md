# Surrounded Regions

## Problem

Given a board of X and O,
capture all regions surrounded by X.


## Idea

Mark border-connected O using DFS.
Convert remaining O to X.


## Algorithm

1. DFS from borders
2. Mark safe cells
3. Convert others
4. Restore safe


## Complexity

Time: O(m * n)

Space: O(m * n)


## Code

See solution.py