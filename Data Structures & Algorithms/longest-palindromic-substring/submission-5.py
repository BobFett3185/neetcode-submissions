class Solution:
    def longestPalindrome(self, s: str) -> str:
    # start at each character and spread left and right. store a local max and return 
        longest = 0
        bigL = 0
        bigR =0
        n = len(s)
        for i in range(0,n): # starting from every charcter 
            palindrome = s[i] # build our word from this
            left = i-1
            right = i+1
            while left > -1 and right < n and s[right] == s[left]:
                palindrome = s[right] + palindrome + s[right]
                left-=1 
                right+=1 
            if len(palindrome) > longest:
                longest = len(palindrome)
                bigL = left+1
                bigR = right

        for i in range(0, n-1):
            palindrome = s[i] + s[i+1]
            if s[i] != s[i+1]:
                continue
            left = i-1
            right = i+2

            while left > -1 and right < n and s[right] == s[left]:
                palindrome = s[right] + palindrome + s[right]
                left-=1 
                right+=1 
            if len(palindrome) > longest:
                longest = len(palindrome)
                bigL = left +1
                bigR = right

        return s[bigL: bigR]

