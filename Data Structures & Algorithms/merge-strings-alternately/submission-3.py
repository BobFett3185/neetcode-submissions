class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        x=min(len(word1), len(word2))
        for i in range(x):
            result.append(word1[i]+word2[i])
        result.append(word1[x:]+word2[x:])
        return "".join(result) # efficient way to do this
