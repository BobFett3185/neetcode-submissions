class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) ==1:
            return 1
        back1 = 1
        back2 = 1 
        current=0
        for i in range(2, len(s)+1): # go through all the characters
            current =0
            if s[i-1] in "123456789":
                current+=back1
            if (s[i-2] =="1" and s[i-1] in "0123456789") or (s[i-2] in "2" and s[i-1] in "0123456"):
                current +=back2
            
            back2 = back1
            back1 = current

        return current 
                

            
        