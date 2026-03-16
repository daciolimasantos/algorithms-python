# Kth Largest Element

## Problem

Find kth largest element in array.


## Idea

Use min heap of size k.


## Algorithm

1. Push into heap
2. Keep size k
3. Pop if bigger
4. Return top


## Complexity

Time: O(n log k)

Space: O(k)


## Code

See solution.py