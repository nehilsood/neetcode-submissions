class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod, suffix_prod = [1]*(n+1),[1]*(n+1)

        for i in range(n):
            prefix_prod[i+1] = prefix_prod[i] * nums[i]
        
        for i in range(n-1,-1,-1):
            suffix_prod[i] = suffix_prod[i+1] * nums[i]

        print(prefix_prod, suffix_prod)
        # return []
        result = [1]*(n+1)
        for i in range(n):
            result[i+1] = prefix_prod[i]*suffix_prod[i+1]
        print(result[1:])
        return result[1:]

        