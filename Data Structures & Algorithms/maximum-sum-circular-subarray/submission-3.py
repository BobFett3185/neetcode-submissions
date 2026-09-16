class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadanes algorithm 
        # useful for finding subarray sum maximum 

        #we find the sum of the subarray ending at that index 
        totalSum = sum(nums)

        result =nums[0] 
        currSum =nums[0]

        currSum2 = nums[0]
        result2 = nums[0]

        for num in nums[1:]:
            if num > currSum+num: # if number greater than adding num 
                currSum = num # replace sum
            else:
                currSum+=num
            result = max(result, currSum) # update result


            if num < currSum2 + num:
                currSum2 = num
            else:
                currSum2 = currSum2+num
            result2 = min(result2, currSum2)

       
        if result2 == totalSum: # if the array is all negative
            return result
        return max(result, totalSum-result2)
            
        
