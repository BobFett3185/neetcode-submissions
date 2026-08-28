class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we can just swap with next number !=k
        read =0
        write = 0
        while read< len(nums):
            if nums[write]!=val:
                write+=1
            elif nums[write]==val and nums[read]!=val:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write+=1 
            read+=1

        return write
            