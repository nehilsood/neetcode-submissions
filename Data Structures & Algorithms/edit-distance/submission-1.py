class Solution:
    def minDistance(self, s: str, p: str) -> int:
        m,n = len(s),len(p)
        cache = {}
        def dfs(i,j):
            #base cases
            if i == m:
                return n - j 
            if j == n:
                return m - i
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i] == p[j]:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)] = min(min(dfs(i+1,j),dfs(i,j+1)),dfs(i+1,j+1)) + 1
            return cache[(i,j)]
        return dfs(0,0)
        