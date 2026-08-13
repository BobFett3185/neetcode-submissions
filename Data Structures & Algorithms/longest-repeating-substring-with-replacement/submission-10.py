class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # move right and update hashmap until subarray becomes invalid 
        # then move the left and update hashmap until 
        l =0 
        charMapping = defaultdict(int) # map characters to frequencies
        mostCommonCount = 0
        result = 0
        for right in range(len(s)):
            charMapping[s[right]] +=1 
            if charMapping[s[right]] > mostCommonCount:
                mostCommonCount = charMapping[s[right]]


            while right-l+1 > mostCommonCount+k:
                charMapping[s[l]]-=1
                l+=1
            result = max(result, right-l+1)
        return result


            # get most commmon chars count
            # if r-l

