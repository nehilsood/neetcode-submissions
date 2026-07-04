class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i,stack):
            if stack < 0: return False # [")"] condition
            if len(s) == i: return stack == 0

            if (i,stack) in dp:
                return dp[(i,stack)]
            if s[i] == "(": 
                dp[(i,stack)] = dfs(i+1,stack+1)
            if s[i] == ")": 
                dp[(i,stack)] = dfs(i+1,stack-1)
            if s[i] == "*": 
                dp[(i,stack)] = (dfs(i+1,stack+1) or dfs(i+1,stack-1) or dfs(i+1,stack))
            return dp[(i,stack)]
        dfs(0,0)
        print(dp)
        return dp[(0,0)]