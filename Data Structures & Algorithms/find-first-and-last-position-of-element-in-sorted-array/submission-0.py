class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # use binary search twice
        l =0 
        r = len(nums)-1
        mid =0

        start =-1
        end = -1 
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                start = mid
                r = mid-1
            elif nums[mid]> target:
                r = mid-1
            else:
                l = mid+1
        print(start)
        l =0 
        r = len(nums)-1
        mid =0
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                end = mid
                l = mid+1
            elif nums[mid]> target:
                r = mid-1
            else:
                l = mid+1

        return [start, end]