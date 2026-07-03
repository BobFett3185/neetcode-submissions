class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # can ignore negative vals and just go through 
        maxSub =nums[0]
        curSum =0
        for n in nums:
            if curSum <0: # if the curSum becomes negative we can reset to 0 to ignore the prev section
                curSum = 0 
            curSum +=n  # always add the next number in subarray 
            maxSub = max(maxSub, curSum) # update the max
        return maxSub
    