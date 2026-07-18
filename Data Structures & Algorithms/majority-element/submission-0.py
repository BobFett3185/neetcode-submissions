class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num]+=1 
            else:
                counts[num]=1
        maxCount =0 
        num =0
        for key in counts.keys():
            if counts[key] > maxCount:
                num = key
                maxCount = counts[key]
        return num