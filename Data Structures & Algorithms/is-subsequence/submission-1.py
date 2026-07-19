class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        for i in range(len(s)):
            char = s[i]
            found = False
            while p<len(t):
                if t[p]==char:
                    found = True
                    p+=1 
                    break
                else:
                    p+=1

            if not found:
                return False 
        return True

        