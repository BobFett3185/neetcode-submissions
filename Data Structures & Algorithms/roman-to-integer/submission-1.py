class Solution:
    def romanToInt(self, s: str) -> int:
        d= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        i=0
        summ=0
        n = len(s)
        while i <n: 
            # you either look at 2 chars or 1:
            if i<n-1 and d[s[i]]<d[s[i+1]]: # make sure you can see 2 numbers and that right one is greater
                summ+=(d[s[i+1]]- d[s[i]])
                i+=2 # bc you used 2 chars
            else: # only consider one char 
                summ+=d[s[i]]
                i+=1 # bc you used only one char
        return summ

        # we can only ever compare 2 numbers or one number