class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we can either start a new subarray or add it to the current 

        currSum, result =0 ,-100000

        for num in nums:
            if num+currSum < num:
                currSum = num 
            else:
                currSum = num+currSum 
            result = max(result, currSum)

        return result
