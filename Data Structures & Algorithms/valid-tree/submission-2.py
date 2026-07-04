class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        cycle detection
        using dfs
        """
        if len(edges) > n - 1:
            return False
        
        #adj list
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        q = collections.deque([(0,-1)])
        visit.add(0)

        while q:
            node,parent = q.popleft()
            for nei in graph[node]:
                if nei == parent: continue
                if nei in visit: return False
                q.append((nei,node))
                visit.add(nei)
        
        return len(visit) == n 
            
        