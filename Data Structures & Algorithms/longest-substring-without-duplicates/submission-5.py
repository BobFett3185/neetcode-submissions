
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set() # use set
        l = 0
        res = 0

        for r in range(len(s)): # loop through the string
            while s[r] in charSet: # you have duplicate 
                charSet.remove(s[l]) # remove from the left until the duplicta is gone
                l += 1
            
            # now that there is no duplicate
            charSet.add(s[r]) # add the character
            res = max(res, r - l + 1) # check new max
        return res




'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 ptr problem

        # have a sliding window 

    # this solution wont work i dont think 
        l =0 
        r = 0 
        maxL =0
        while True:
            r+=1 
            if s[r] == s[l]: # if there is a duplicate 
                length = r-l
                maxL = max(length, maxL)
                l+=1 
                r=l
            
            if r == len(s)-1:
                return maxL
'''