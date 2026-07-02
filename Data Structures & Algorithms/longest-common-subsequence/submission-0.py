class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #bottom up building subsequence from empty string
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1): # work backwards along the columns
            for j in range(len(text2)-1, -1, -1): # work back along the row 
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1] #if they match add one to the diagonal 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) #max between previous spots 
        return dp[0][0]
