class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # go through and have a read and write pointer
        # if last 2 numbers are not this number then we are able to write it!

        read =0 
        write =0 
        while read<len(nums):
            if write>1 and nums[write-1]==nums[read] and nums[write-2] == nums[read]:
                read+=1
            else:
                nums[write]= nums[read]
                write+=1 
                read+=1 
        return write