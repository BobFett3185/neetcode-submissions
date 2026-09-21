class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = defaultdict(int)
        
        for index,char in enumerate(s):
            map[char]+=1 
        for index,char in enumerate(s):
            if map[char]==1:
                return index
        return -1

        
