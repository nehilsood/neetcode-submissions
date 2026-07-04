class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            # handle duplicate
            if nums[k] > 0:
                break
            if k >0 and nums[k] == nums[k -1]:
                continue
            target = -1 * nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                temp_sum = nums[i] + nums[j]
                if temp_sum == target:
                    res.append([nums[i],nums[j],nums[k]])
                    i += 1
                    j -= 1
                    while i<j and nums[i] == nums[i-1]:
                        i += 1
                    while i<j and nums[j] == nums[j+1]:
                        j -= 1
                elif temp_sum > target:
                    j -= 1
                else:
                    i += 1
        
        return res


        