class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = defaultdict(int)
        for index,char in enumerate(s):
            if char in map:
                map[char]=len(s)
            else:
                map[char]= index
        
        result = len(s)+1
        for value in map.values():
            result = min(value, result)
        
        if result == len(s):
            return -1
        return result