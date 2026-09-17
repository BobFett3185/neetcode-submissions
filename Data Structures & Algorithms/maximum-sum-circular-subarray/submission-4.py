class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadanes algorithm is useful for finding subarray sum maximum 
        #we find the sum of the subarray ending at that index 

        totalSum = sum(nums) # sum of whole array

        result =nums[0]  #vars we need
        currSum =nums[0]
        currSum2 = nums[0]
        result2 = nums[0]

        for num in nums[1:]: # for all the rest of the numbers
            if num > currSum+num: # if we should start new subarry
                currSum = num
            else: # continue with same subarray
                currSum+=num
            result = max(result, currSum) # update result

            # we find the minimum subarray as well
            if num < currSum2 + num:
                currSum2 = num
            else:
                currSum2 = currSum2+num
            result2 = min(result2, currSum2)

       
        if result2 == totalSum: # if the array is all negative
            return result
        return max(result, totalSum-result2)

        '''
        we find both the maximum subarray and minimum subarray. 
        The minterm helps us in the chance that the real max is flowing over   on both end, so we subtract that min subarray from the total amount
        then we return the max of our 2 possiblities
        '''
            
        
