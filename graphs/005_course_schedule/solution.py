class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        graph = {i: [] for i in range(numCourses)}
        
        for a, b in prerequisites:
            graph[a].append(b)
            
        state = [0] * numCourses
        
        def dfs(node):
            
            if state[node] == 1:
                return False
            
            if state[node] == 2:
                return True
            
            state[node] = 1
            
            for nei in graph[node]:
                
                if not dfs(nei):
                    return False
            
            state[node] = 2
            
            return True
        
        for i in range(numCourses):
            
            if not dfs(i):
                return False
            
        return True