class Solution:
    def isValid(self, s: str) -> bool:
        match = {"]":"[","}":"{",")":"("}
        stack = []
        for par in s:
            if par in match.values():
                stack.append(par)
            elif stack and par not in match.values():
                if stack[-1] == match[par]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0

        