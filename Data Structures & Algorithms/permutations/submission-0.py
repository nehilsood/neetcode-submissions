class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        visited = set()
        def dfs(permutation,visited):
            if len(permutation) == n:
                result.append(permutation.copy())
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                permutation.append(nums[i])
                visited.add(nums[i])
                dfs(permutation,visited)
                visited.remove(nums[i])
                permutation.pop()
        dfs([],visited)
        return result


        