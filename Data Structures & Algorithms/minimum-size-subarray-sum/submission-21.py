class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # use sliding window
        l = 0 
        currSum =0
        result = len(nums)+1
        for r in range(len(nums)):
            currSum+=nums[r]
            while currSum>=target:
                result = min(result, r-l+1)
                currSum-=nums[l]
                l+=1
                
            r+=1

        if result ==len(nums)+1:
            return 0
        else:
            return result
