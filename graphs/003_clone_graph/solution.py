class Node:
    def __init__(self, val=0, neighbors=None):
        self.val  = val
        self.neighbors = self.neighbors if neighbors else []

class Solution:
    def cloneGrapph(self, node):
        
        if not node:
            return None
        
        old_to_new = {}
        
        def dfs(n):
            
            if n in old_to_new:
                return old_to_new[n]
            
            copy = Node(n.val)
            old_to_new[n]  = copy
            
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return ccopy
        
        return dfs(node)