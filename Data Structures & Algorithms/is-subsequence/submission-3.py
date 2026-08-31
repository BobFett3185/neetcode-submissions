class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tp=0 
        sp=0
        while sp<len(s):
            char = s[sp] 
               
            while tp<len(t) and t[tp] != char:
                tp+=1 
        
            if tp >= len(t) or t[tp]!=char:
                return False
            sp+=1
            tp+=1
        return True
        