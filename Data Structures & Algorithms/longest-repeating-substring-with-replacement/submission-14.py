class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        result = 0 
        mostFreq = 0
        '''
        we go through and have a sliding window, add char 
        if we break it, fix it by removing from window until length - most frequent = k 
        then update result and go to next iteration
        '''

        left =0 
        for right, char in enumerate(s):
            counts[char]+=1
            mostFreq = max(mostFreq, counts[char])
            while right - left +1 - mostFreq > k:
                counts[s[left]]-=1
                left+=1
            result = max(result, right-left+1)
        return result
