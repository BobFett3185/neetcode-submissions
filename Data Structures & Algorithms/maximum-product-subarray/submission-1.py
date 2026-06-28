class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # go through and keep track of min and max to account for negative back and forth 
        result = max(nums)
        curMin, curMax = 1,1 
        for n in nums: # go through all the numbers
            temp = curMax # save this
            curMax = max(n*curMax, n*curMin, n) # current max can be updated by multipliying by the min or max 
            curMin = min(n*temp, n*curMin, n) # same for the min 
            # this helps us account for negative values flipping stuff back and forth
            result = max(result,curMax) # save our largest 
        return result
