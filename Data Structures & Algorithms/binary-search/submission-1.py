class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            mid = (i+j)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                j = mid
            else:
                i = mid + 1
        return -1
        