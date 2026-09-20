class Solution:
    def decodeString(self, s: str) -> str:
        # when we hit a [ we need to save the number 

        # build a number  - stop when you hit a brakcet and store number in stack 
        # start building string, 
        # if you hit another bracket, push that string to stack and then put number onto 

        letterStack = []
        numStack = []
        number = 0
        build = ""
        for char in s:
            # 4 cases:
            if char.isdigit():
                number = number*10 + int(char) # update number

            elif char.isalpha():
                build+=char # update chars
            
            elif char == '[':
                numStack.append(number)
                letterStack.append(build)

                number = 0
                build = ""
            
            else:# grab prev state and update result
                repeats = numStack.pop()
                prev = letterStack.pop()
            
                build = prev+ build*repeats
        return build
            
            
