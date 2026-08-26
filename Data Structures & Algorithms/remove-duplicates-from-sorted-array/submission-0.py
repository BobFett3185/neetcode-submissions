class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current =0 
        
        while current < len(nums):
            num = nums[current]
            forward = current+1
            while forward<len(nums) and nums[forward]== num :
                nums.pop(forward)
            current+=1
        return len(nums)

        