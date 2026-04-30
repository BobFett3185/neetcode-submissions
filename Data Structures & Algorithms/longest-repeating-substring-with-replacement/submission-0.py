class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #find longest substring of same character but it can have k other characters in it 
        
        #inititalize a count to keep track of counts of letters 
        count = {}
        result =0; 
        l=0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0) #increment count of s[r]

            while (r-l+1) - max(count.values()) > k: # while length - number of most occuring letters > 1
                count[s[l]]-=1 # decrement current l pointer letter
                l+=1  # move the right pointer up one

            result = max(result , r-l+1) # update the result with length if it greater

        return result
#logic is really confusing