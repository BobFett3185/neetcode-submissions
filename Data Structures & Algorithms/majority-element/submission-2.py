class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ans = -1
        for num in nums:
            if count==0: # if the count is 0 then set new ans and increment count
                ans = num
                count+=1
            else: # if there is a count of some number
                if num!= ans: # if we dont have that number decrement counter
                    count-=1 
                else: # otherwise increment that count
                    count+=1
        # we use the count as a way to see if some other number takes its place and overpowers it 
        
            
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