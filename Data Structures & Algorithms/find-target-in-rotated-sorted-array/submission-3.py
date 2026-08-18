class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search 
        # search value always in range 
        # shrink our range
        l =0 
        r = len(nums)-1
        while l<=r:
            mid = (r+l)//2
            if target == nums[mid]:
                return mid
            # one portion will always be sorted 

            # if left portion sorted 
            if nums[mid]>= nums[l]:
                # if we fit in here 
                if target>=nums[l] and target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            
            elif nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l= mid+1
                else:
                    r = mid-1
        
        return -1
