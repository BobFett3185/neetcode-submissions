class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": # if we have a starting 0 its invalid
            return 0
        if len(s) ==1: # if only char then return 1 
            return 1

        back1 = 1 # we only need to look back 2 spots to keep track of ways to decode the first i charcacters 
        back2 = 1 

        # keep a current 
        current=0
        # from second index through all the chars
        for i in range(2, len(s)+1): # go through all the characters
            current =0
            if s[i-1] in "123456789": # if the previous one is not 0 then we can add the number of paths up to that point 
                current+=back1
# If the current digit can stand alone, then every valid decoding up to position i-1 can be extended by this digit.

            # this checks if we can add all the paths which would have lead up to us using it as a 2 num value 
            if (s[i-2] =="1" and s[i-1] in "0123456789") or (s[i-2] in "2" and s[i-1] in "0123456"):
                current +=back2
#If the last two digits form a valid letter (10-26), then every valid decoding up to position i-2 can be extended by that 2-digit letter.
            
            # move pointers
            back2 = back1
            back1 = current

        return current  # return
                

            
        