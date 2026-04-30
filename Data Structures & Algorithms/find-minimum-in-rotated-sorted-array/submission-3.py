class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search is log n 

        l = 0
        r = len(nums)-1

        while l<r:
            m = (l+r-1)// 2

            if nums[r]> nums[m]:
                r =m 
            else :
                l = m+1 
        return nums[l]
                
            

        
        