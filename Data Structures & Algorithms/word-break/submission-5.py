class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #bottom up approach with tabulation 
        dp = [False]*(len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1): # go from the back 
            for w in wordDict:
                if i + len(w) <= len(s): # if it has enough chars to be compared 
                    if s[i: i+len(w)] == w: # and if that part of the string is equal to our word 
                        dp[i] = dp[i + len(w)] # then dp[i] = True if rest of word has a match
                        # we bascially make sure that the end of the chunk ends where another chunk starts 
                        # and that there is no missing chars in between 
                if dp[i]:
                    break 
        return dp[0]