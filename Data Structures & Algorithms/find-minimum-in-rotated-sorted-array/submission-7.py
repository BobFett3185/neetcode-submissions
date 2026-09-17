class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we rely on an imprtant property, at least one side will be sorted

        l =0 
        r=len(nums)-1
        

        while l<r:
            mid = (l+r)//2
            # check if left or right side is sorted 
            if nums[mid]>nums[r]: # if the left side is sorted 
               l = mid+1
            else:
                r=mid
        return nums[l]

                
