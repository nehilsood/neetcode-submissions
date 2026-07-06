class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in _dict:
                return [_dict[diff],i]
            else:
                _dict[nums[i]] = i
        


        