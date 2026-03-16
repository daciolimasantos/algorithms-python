from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            
        queue = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        taken = 0
        
        while queue:
            
            node = queue.popleft()
            taken += 1
            
            for nei in graph[node]:
                
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return taken == numCourses