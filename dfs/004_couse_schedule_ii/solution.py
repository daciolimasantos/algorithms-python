class Solution:
    def findOrder(sel, numCourses, prerequisites):
        
        graph = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            
        visit = set()
        cycle = set()
        order = []
        
        def dfs(node):
            
            if node in cycle:
                return False
            
            if node in visit:
                return True
            
            cycle.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            cycle.remove(node)
            visit.add(node)
            order.append(node)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return order [::-1]