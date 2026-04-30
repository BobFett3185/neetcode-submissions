class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove the whitespace
        # compare first and last index...
        str =[]
        for char in s:
            if char.isalpha() or char.isdigit():
                str.append(char)

        for i in range(len(str)):
            if str[i].lower() != str[len(str)-1-i].lower():
                return False
        return True



        
        