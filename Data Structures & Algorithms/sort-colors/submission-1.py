class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we maintain a write pointer for both the left and right side 
        # we basically want to move the 0s the front and the 2s to the back 

        left =0 
        right = len(nums)-1
        read = 0 

        while read<=right:
            if nums[read]==0:# swap with left then left+1
                temp = nums[read]
                nums[read] = nums[left]
                nums[left]= temp
                left+=1
                read+=1
            elif nums[read]==2:
                temp = nums[read]
                nums[read] = nums[right]
                nums[right]= temp
                right-=1
            else:
                read+=1
            