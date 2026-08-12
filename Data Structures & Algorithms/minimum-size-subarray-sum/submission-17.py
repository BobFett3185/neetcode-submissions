class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # use sliding window approach 
        # keep a left and right window and move right while target is 
        result = 100000
        left = 0 
        localSum =0
        for right in range(len(nums)):
            localSum+=nums[right]
            while localSum >= target: # if gone over -> shrink and check still valid
                result = min(result, right-left+1)
                localSum -= nums[left]
                left+=1
        if result != 100000:
            return result
        return 0 
            



            



    '''suboptimal solution:
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
            
        if result != 100000:nums):

$0
            return result
        return 0 
'''