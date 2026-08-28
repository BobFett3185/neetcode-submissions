class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we need a 2 poitner approach wehre one is read and one is write 

        # we read forward and if there is a 0 at write and non zero at read we can swap 


        # go through and overwrite with non zero values 
        # then fill rest of array with 0s 

        read =0
        write =0 

        while read<len(nums):
            if nums[read]!=0:
                nums[write] =nums[read]
                write+=1 
            read+=1 
        for i in range(write, len(nums)):
            nums[i]=0 
        
        