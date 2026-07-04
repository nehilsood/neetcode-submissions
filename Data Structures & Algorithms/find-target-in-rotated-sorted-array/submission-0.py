class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot
        n = len(nums)
        pivot = 0
        l,r = 0,n-1
        
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m +1
            else:
                r = m
        
        pivot = l

        if target > nums[-1]:
            l,r = 0,pivot
        else:
            l,r = pivot,n
        
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid+1
        
        return -1





        
                

        