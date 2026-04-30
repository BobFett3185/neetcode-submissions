class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to allow for fast lookup
        numSet = set(nums)
        longest =0 # keep track of longest 

        for num in nums: # iterate through all numbers
            if num - 1 not in numSet: # only checks for sequences if previous num not there
                length =0
                while num + length in numSet: # if next number is there
                    length +=1   # increment length 
                if length > longest: # if its more that longest
                    longest = length
        return longest
            
        