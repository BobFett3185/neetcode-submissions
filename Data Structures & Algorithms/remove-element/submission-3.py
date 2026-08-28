class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we can just swap with next number !=k
        read =0
        write = 0
        while read< len(nums):
            if nums[read]!=val:
                nums[write] = nums[read]
                write+=1
            read+=1

        return write
            