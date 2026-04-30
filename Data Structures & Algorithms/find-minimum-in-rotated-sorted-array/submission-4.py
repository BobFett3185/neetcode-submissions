class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search is log n 

        l = 0
        r = len(nums)-1

        while l<r: # binary search 
            m = (l+r-1)// 2 # have some middle

            if nums[r]> nums[m]:   # if right is greater than mid then everything
                                    # in between is not the min so change bound 
                r =m 
            else : # same idea here 
                l = m+1 
        return nums[l]# return left ptr which should be least element
                
            

        
        