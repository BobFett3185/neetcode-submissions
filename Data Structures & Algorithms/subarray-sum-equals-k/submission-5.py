class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0]=1
        # make prefix sums nd after we make one, update result
        result =0
        prefixSum =0 
        for i in range(len(nums)):
            prefixSum+=nums[i]

            result+=seen[prefixSum - k]
            seen[prefixSum]+=1 
            
        return result


