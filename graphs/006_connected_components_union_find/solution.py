class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self, x, y):
        
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return 0
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
            
        return 1
    
class Solution:
    def countComponents(self, n, edges):
        
        uf = UnionFind(n)
        
        components = n
        
        for a, b in edges:
            components -= uf.union(a, b)
            
        return components