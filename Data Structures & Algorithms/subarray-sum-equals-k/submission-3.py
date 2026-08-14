class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        prefixSums=[0]*(len(nums)+1)

        # make prefix sums and add them to our seen map
        for i in range(len(nums)):
            count = i+1
            prefixSums[count] = prefixSums[i]+nums[i]
        
        # now go through prefix sums 
        result =0 
        for n in prefixSums:
            result+=seen[n-k]
            seen[n]+=1 
        return result


