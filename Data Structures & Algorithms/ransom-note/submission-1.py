class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # build a hash set where key is the letter and value is the count 
        counts = {}
        for letter in magazine:
            if letter in counts:
                counts[letter]+=1
            else:
                counts[letter] =1
        
        # then check if letters can be built from counts
        for letter in ransomNote:
            if letter in counts:
                if counts[letter]==1:
                    del counts[letter]
                else:
                    counts[letter]-=1
            else:
                return False
        return True

        