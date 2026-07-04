import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        for num in nums[1:]:
            idx = bisect.bisect_left(tail,num)
            if idx == len(tail):
                tail.append(num)
            else:
                tail[idx] = num
        
        return len(tail)

        