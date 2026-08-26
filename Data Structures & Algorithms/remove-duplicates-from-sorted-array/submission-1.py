class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 1
        forward =1
        
        while forward<len(nums):
            if nums[forward] != nums[current-1]:
                nums[current]=nums[forward]
                current+=1 

            # move forward to find a new number each iteration
            forward+=1 
        
        return current
        
# dont pop, just overwrite at current when we see a new number
        