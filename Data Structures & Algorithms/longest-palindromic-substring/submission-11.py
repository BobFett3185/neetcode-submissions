class Solution:
    def longestPalindrome(self, s: str) -> str:
        #maybe use a sliding window technique 
        result =0
        ans = ""

        #do expansion around the center
        for i in range(len(s)):
            l = i-1
            r = i+1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1

            if result< r-l-1:
                result = r-l-1 # have to remove the 2 invalid l, r places
                ans = s[l+1:r] # then valid palindrome is this one
        
        for i in range(len(s)-1):
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1

            if result < r-l-1: 
                result = r-l-1
                ans = s[l+1:r]

        return ans

            
