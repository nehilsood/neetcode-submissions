from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #adjacency graph
        graph = defaultdict(list)
        visited = [False]*n
        for edge in edges:
            x,y = edge[0], edge[1]
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            for child in graph[node]:
                if not visited[child]:
                    visited[child] = True
                    dfs(child)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        return res
        