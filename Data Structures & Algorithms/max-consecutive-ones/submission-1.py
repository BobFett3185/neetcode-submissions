class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result =0
        count =0
        for num in nums:
            if num ==1:
                count+=1 
            if num == 0:
                result = max(count, result)
                count = 0
        return max(result,count)