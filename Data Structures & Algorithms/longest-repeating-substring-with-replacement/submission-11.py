class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # move right and update hashmap until subarray becomes invalid 
        # then move the left and update hashmap until 
        l =0 
        charMapping = defaultdict(int) # map characters to frequencies
        mostCommonCount = 0
        result = 0
        for right in range(len(s)): # use for loop for the right pointer
            charMapping[s[right]] +=1 #update frequency map and mostCommonCount
            if charMapping[s[right]] > mostCommonCount:
                mostCommonCount = charMapping[s[right]]

            while right-l+1 > mostCommonCount+k: # if len > count of most common char + k
                charMapping[s[l]]-=1 # then we need to remove left until valid
                l+=1
            result = max(result, right-l+1) # return the length of the valid subarray
        return result
