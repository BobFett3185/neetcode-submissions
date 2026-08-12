class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 100000
        for l in range(len(nums)):
            localSum = nums[l]

            r = l+1
            while localSum<target and r<len(nums):
                localSum+=nums[r]
                r+=1
            if localSum>=target:
                result = min(result, r-l)
                print(result)
            
        if result != 100000:
            return result
        return 0 
