# Top K Frequent Elements

## Problem

Return k most frequent elements.


## Idea

Use hashmap to count.
Use heap to keep top k.


## Algorithm

1. Count frequency
2. Push into heap
3. Keep size k
4. Return elements


## Complexity

Time: O(n log k)

Space: O(n)


## Code

See solution.py