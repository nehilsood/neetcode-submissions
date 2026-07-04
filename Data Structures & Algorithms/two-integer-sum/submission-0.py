class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,num in enumerate(nums):
            temp = target - num
            if temp in res:
                return [res[temp],i]
            res[num] = i
                

        