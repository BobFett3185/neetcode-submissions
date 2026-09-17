class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find elements counts 
        # then find frequency of counts

        freq = [[]for i in range(len(nums)+1)] #create an array for all possible frequencies of any element in nums
        counts = defaultdict(int)

        for num in nums:
            counts[num]+=1
        for key, value in counts.items():
            freq[value].append(key)
        
        result=[]
        for i in range(len(freq)-1, -1,-1): # go backward through freuency array
            for num in freq[i]:
                result.append(num)
            if len(result) == k:
                return result

