class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(nums):
            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            
            return dp[-1]
        
        if len(nums) <= 2:
            return max(nums)
        return max(rob2(nums[1:]),rob2(nums[:-1]))
        