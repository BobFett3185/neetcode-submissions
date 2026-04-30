class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            count= [0]*26 # create a count array for each word
            for char in word:
                count[ord(char) - ord("a")] +=1 # add ascii value to array 
                # ord returns the ascii value!!! 
            key = tuple(count) #convert key to tuple which is hashable
            if key not in map: # if that count pattern is not there then 
                map[key] = [] #then make the pair array 
            map[key].append(word)

        return list(map.values())

#the idea here is that you use an array containing the 
#frequency of characters in the word as the key for the hash map
            

