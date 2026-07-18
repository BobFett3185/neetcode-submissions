class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        # key can be a hashmap of the counts of the letters in a word
        
        for word in strs:
            arr = [0]*26
            for char in word:
                arr[ord(char)-ord('a')]+=1
            tup = tuple(arr)
            if tup in result:
                result[tup].append(word)
            else:
                result[tup] = [word]
        r = []
        for value in result.values():
            r.append(value)
        return r