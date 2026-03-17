# Kth Largest Element

## Problem

Find kth largest element.


## Idea

Use min heap size k.


## Algorithm

1. push
2. if > k pop
3. return heap[0]


## Complexity

Time: O(n log k)

Space: O(k)


## Code

See solution.py