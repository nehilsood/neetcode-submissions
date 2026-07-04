class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        while l < r:
            _sum = nums[l] + nums[r] 
            if _sum == t:
                return [l+1,r+1]
            elif _sum < t:
                l += 1
            else:
                r -= 1
            