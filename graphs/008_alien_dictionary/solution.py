from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        
        graph = defaultdict(set)
        indegree = {}
        
        for word in words:
            for c in word:
                indegree[c] = 0
                
        for i in range(len(words) - 1):
            
            w1 = words[i]
            w2 = words[i + 1]
            
            for j in range(min(len(w1), len(w2))):
                
                if w1[j] != w2[j]:
                    
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                        
                    break
                
        queue = deque()
        
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
                
        res = []
        
        while queue:
            
            c = queue.popleft()
            res.append(c)
            
            for nei in graph[c]:
                
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)