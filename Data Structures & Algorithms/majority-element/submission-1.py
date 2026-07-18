class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ans = -1
        for num in nums:
            if count ==0:
                ans = num
                count+=1
            else:
                if num!= ans:
                    count-=1 
                else:
                    count+=1
            
        return ans 


        
        
        
        
        '''
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
        '''