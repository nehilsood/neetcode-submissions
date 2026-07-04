class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        lcs = 0

        for num in nums:
            if (num-1) not in hashset:
                streak = 1
                while (num+streak) in hashset:
                    streak += 1
                lcs = max(streak,lcs)
        
        return lcs

        