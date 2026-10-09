from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(a):
            p = parent[a]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
    
            return p
    
        def union(a, b):
            a, b = find(a), find(b)
    
            if a == b:
                return False
    
            if rank[a] > rank[b]:
                parent[b] = a
                rank[a] += rank[b]
    
            else:
                parent[a] = b
                rank[b] += rank[a]
    
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]