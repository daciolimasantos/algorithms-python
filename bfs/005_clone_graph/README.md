# Clone Graph

## Problem

Given a node in a graph,
return a deep copy of the graph.


## Idea

Use BFS and a dictionary
to map original nodes to cloned nodes.


## Algorithm

1. Use queue for BFS
2. Create clone for each node
3. Store in dict
4. Connect neighbors
5. Return clone


## Complexity

Time: O(V + E)

Space: O(V)


## Code

See solution.py