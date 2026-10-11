class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make frequency array 
        freq = [[]for j in range(len(nums)+1)]

        result =[]
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        for key, value in count.items(): #we want to add to our frequency array
            freq[value].append(key)
        
        for i in range(len(freq)-1, -1, -1):
            if len(freq[i])>0:
                for f in freq[i]:
                    result.append(f)
        return result[0:k]