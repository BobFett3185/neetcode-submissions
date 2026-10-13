class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left =0 
        right = len(nums)-1
        

        while left<= right:
            # find which part is sorted 
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[right] > nums[mid]:
                if target > nums[mid] and target <= nums[right]: # in sorted portion
                    left = mid+1
                else:
                    right = mid
            else:#left part sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid 
                else:
                    left = mid+1
            
        return -1
