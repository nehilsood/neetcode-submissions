class Solution:
    def minDistance(self, s: str, p: str) -> int:
        m,n = len(s),len(p)

        def dfs(i,j):
            #base cases
            if i == m:
                return n - j 
            if j == n:
                return m - i
            if s[i] == p[j]:
                return dfs(i+1,j+1)
            return min(min(dfs(i+1,j),dfs(i,j+1)),dfs(i+1,j+1)) + 1
        return dfs(0,0)
        