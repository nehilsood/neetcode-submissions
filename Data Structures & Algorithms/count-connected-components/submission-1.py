from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #adjacency graph
        graph = defaultdict(list)
        visited = [False]*n
        for edge in edges:
            x,y = edge[0], edge[1]
            graph[x].append(y)
            graph[y].append(x)

        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                cur = q.popleft()
                for child in graph[cur]:
                    if not visited[child]:
                        visited[child] = True
                        q.append(child)

        
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                bfs(node)
                res += 1
        return res
        