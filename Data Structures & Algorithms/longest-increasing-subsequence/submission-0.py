class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # probably bottom up so we need to build up from the end 
        lis = [1]*len(nums)

        for i in range(len(nums)-1, -1, -1): # work backwards from end 
            for j in range(i+1, len(nums)): # go forward to end of array 
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        return max(lis)

