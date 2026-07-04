class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n

    def find(self,node):
        if self.parent[node] == node: # leader
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    def union(self,x,y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False
        if self.rank[parent_y] > self.rank[parent_x]:
            parent_x,parent_y = parent_y, parent_x
        self.parent[parent_y] = parent_x
        self.rank[parent_x] += self.parent[parent_y]
        return True
        
        


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #union find
        res = n
        dsu = UnionFind(n)
        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        
        return res

            
        