class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        x=min(len(word1), len(word2))
        for i in range(x):
            result+=(word1[i]+word2[i])
        return result+word1[x:]+word2[x:]