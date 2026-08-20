class Solution:
    def isPalindrome(self, s: str) -> bool:
        l =0 
        r = len(s)-1
        while l<=r:
            while not s[l].isalnum() and l<len(s)-1:
                print (s[l])
                print(l)
                l+=1
            while not s[r].isalnum() and r> -1:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1 
            r-=1 
        return True