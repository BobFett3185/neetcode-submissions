class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = {"(", "{", "["}
        # we add openings to the stack and then when we hit a closing check if correct closing in the stack 
        if len(s)%2 == 1:
            return False

        for char in s:
            if char in openings:
                stack.append(char)
            elif len(stack)==0:
                return False
            elif char == "]" and stack.pop()!="[":
                return False
            elif char == "}" and stack.pop()!="{":
                return False
            elif char == ")" and stack.pop()!="(":
                return False
            else:
                continue
        if len(stack)==0:
            return True
        return False


