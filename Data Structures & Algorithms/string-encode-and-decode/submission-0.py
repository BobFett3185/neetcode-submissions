class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i])) + "#" + strs[i]
        return s


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0   # current index 
        while i < len(s):
            j= i # j is a index that goes to the next word 
            while s[j] != "#":
                j+=1 
            length = int(s[i:j])
            i= j+1 # i skips past # -- to start of word
            j = i+ length # j skips past word 

            result.append(s[i:j]) # then add word to result 
            i = j # now bring i to the start of next number, #, word  
        return result
