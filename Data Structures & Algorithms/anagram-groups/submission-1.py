class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        # key can be a hashmap of the counts of the letters in a word
        # value is an array of

        for word in strs:
            arr = []
            for letter in word:
                arr.append(letter)
            arr.sort()
            key =""
            for char in arr:
                key+=char
            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]

        r =[]
        for value in result.values():
            r.append(value)
        return r