class Solution:
    def longestCommonSubsequence(self, s: str, p: str) -> int:
        cache = {}
        def dfs(i,j):
            if i == len(s) or j == len(p):
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]

            if s[i] == p[j]:
                cache[(i,j)] = 1 + dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)] = max(dfs(i+1,j),dfs(i,j+1))
            return cache[(i,j)]
        
        return dfs(0,0)
        