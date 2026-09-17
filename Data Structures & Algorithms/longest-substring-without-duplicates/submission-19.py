class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window pattern 

        l = 0 
        seen = set()
        result =0 
        for r in range(len(s)):
            # we check if right is already seen
            while s[r] in seen:
                seen.remove(s[l])
                l+=1 
            seen.add(s[r])
            result = max(result, r-l+1)
        return result