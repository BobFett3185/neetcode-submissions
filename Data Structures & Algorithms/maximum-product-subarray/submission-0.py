class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # go through and keep track of min and max to account for negative back and forth 
        result = max(nums)
        curMin, curMax = 1,1
        for n in nums:
            temp = curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(n*temp, n*curMin, n)
            result = max(result,curMax)
        return result
