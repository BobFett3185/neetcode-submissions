class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we basically need to have a mapping of a list of characters to a list of words that are anagrams of that 

        mapping = {}
        for string in strs:
            arr = [0]*26 #an array the couunts of all 26 letters
            for char in string:
                arr[ord(char)-ord('a')]+=1
            
            arr = tuple(arr)
            if arr in mapping:
                mapping[arr].append(string)
            else:
                mapping[arr]=[string] 
        result = []
        for value in mapping.values():
            result.append(value)

        return result



            
