# Course Schedule

## Problem

You are given number of courses and prerequisites.

Return true if you can finish all courses.


## Idea

Use BFS Topological Sort.

Count indegree.
Start from nodes with indegree 0.


## Algorithm

1. Build graph
2. Compute indegree
3. Push indegree 0 to queue
4. BFS
5. Count visited
6. Check if all visited


## Complexity

Time: O(V + E)

Space: O(V + E)


## Code

See solution.py