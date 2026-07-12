class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # could just loop through and mark numbers as found in a hash map 
        # then go back through hash map and find which one is not found and output it 
        # requires O(n) time and space 

        # we can do in constant space with binary exlusive or 
        # exlusive or all the numbers 0-n and exlusive or all numbers from 0 to n with a missing one
        # all the numbers in common in both sets will cancel each other out in the ^ 
        # and you will be left with the missing number 

        # or you could just add the index and subtract from actual values 
        # index goes from 0 to n-1 and values go from 0 to n (actual array)
        # then add back n

        res = 0
        for i in range(len(nums)):
            res+= (i-nums[i])
        return res+len(nums)



