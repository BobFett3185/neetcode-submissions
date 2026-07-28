class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # go through and use a set and check if char alr in set 
        if s == "" or s == " ":
            return len(s)
        seen = set()
        l =0
        r=0
        result =0 

#pwwkew - [pw]
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
                
            result = max(result, r-l+1)
        return result
            