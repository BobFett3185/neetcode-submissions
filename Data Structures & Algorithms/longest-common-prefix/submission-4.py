class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = []
        i = 0 

        while True:
            if i == len(strs[0]):
                return "".join(prefix)
            char = strs[0][i]
            for word in strs:
                if i == len(word):
                    return "".join(prefix)
                if word[i] != char:
                    return "".join(prefix)
            prefix.append(char)
            i+=1

        # we keep a position count 
        # then get the char from first word 
        # then from there we can check if the rest of the words have that character in that position 

        

        
                
