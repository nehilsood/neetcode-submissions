class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # return 0
        if not s1 or not s2: return 0
        if len(s1) >= len(s2):
            s1,s2 = s2,s1
        _dict = {}
        def dfs(i,j):
            if i == len(s1) or j == len(s2):
                _dict[(i,j)] = 0
            if (i,j) in _dict: 
                return _dict[(i,j)]
            if s1[i] == s2[j]: 
                _dict[(i,j)] =  1 + dfs(i+1,j+1)
            else:
                _dict[(i,j)] =  max(dfs(i+1,j), dfs(i,j+1))
            return _dict[(i,j)]
        return dfs(0,0)
        
        


        
        

        