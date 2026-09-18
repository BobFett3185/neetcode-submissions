class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums)+1)
        count =0
        mymap = defaultdict(int)
        mymap[0]=1
        i=1

        for num in nums:
            prefix[i] = prefix[i-1]+num
            
            if prefix[i]-k in mymap:
                count+=mymap[prefix[i]-k]

            mymap[prefix[i]]+=1
            i+=1
            
        return count