class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        can use a prefix sum 
        then we can go through and check if differnce is a prefix sum 
        then we can store the counts of prefix sums in the msp 
        '''
        result =0 
        counts =defaultdict(int)
        counts[0]=1
        prefixSums = [0]
        for i, num in enumerate(nums):
            prefixSums.append(num+prefixSums[-1])
            result+=counts[prefixSums[-1]-k]
            counts[prefixSums[-1]]+=1
        
        # we can go through the nums and check if prefix sum - k is in our map 
        

            
        return result



