class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window -- consecutive number, subarray 
        numMap = defaultdict(int)
        l=0
        result =0
        for r in range(len(nums)):
            numMap[nums[r]]+=1 # process a number 

            while r - l + 1 - numMap[1]>k:
                numMap[nums[l]]-=1
                l+=1
            
            result = max(result, r - l + 1)

        return result

            

        