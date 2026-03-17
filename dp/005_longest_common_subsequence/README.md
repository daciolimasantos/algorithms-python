# Longest Common Subsequence

## Problem

Find LCS of two strings.


## Idea

DP 2D

if equal:
  +1 diagonal

else:
  max left/up


## Algorithm

1. build dp table
2. compare chars
3. update dp
4. return last cell


## Complexity

Time: O(m*n)

Space: O(m*n)


## Code

See solution.py