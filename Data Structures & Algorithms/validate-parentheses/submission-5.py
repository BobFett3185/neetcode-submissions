class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char) # push to stack 

            else:
                if len(stack) ==0 :
                    return False
                a = stack.pop()
                if a != '(' and char == ')':
                    return False 
                elif a != '[' and char == ']':
                    return False
                elif a != '{' and char == '}':
                    return False
            

        if len(stack) !=0:
            return False
        return True
                


                


            