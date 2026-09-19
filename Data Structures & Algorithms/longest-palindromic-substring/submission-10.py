class Solution:
    def longestPalindrome(self, s: str) -> str:
        #maybe use a sliding window technique 
        result =0
        ans = ""

        #do expansion around the center
        for i in range(len(s)):
            middle = s[i]
            l = i-1
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if result< r-l-1:
                result = r-l-1
                ans = s[l+1:r]
        
        for i in range(len(s)-1):
            middle = s[i]+s[i+1]
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if result < r-l-1:
                result = r-l-1
                ans = s[l+1:r]
        return ans

            
