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
            else: # if s[r] is seen
                while s[r] in seen:
                    seen.remove(s[l]) # then keep removing from the left until right not seen anymore 
                    l+=1
                seen.add(s[r]) # then add right back
                
            result = max(result, r-l+1)#update the result
        return result
            