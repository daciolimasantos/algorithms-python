from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []
        
class Solution:
    def cloneGraph(self, node):
        
        if not node:
            return None
        
        clones = {}
        
        queue = deque([node])
        
        clones[node] = Node(node.val)
        
        while queue:
            
            current = queue.popleft()
            
            for nei in current.neighbors:
                
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    queue.append(nei)
                    
                clones[current].neighbors.append(
                    clones[nei]
                )
        
        return clones[node]