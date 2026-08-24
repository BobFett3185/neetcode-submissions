class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        use a stack and put letters in stack, if oper, pop 2 and put result in stack 
        '''
        mystack = []
        operators = ['+','-','*','/']

        for token in tokens:

            if token in operators:
                num2 = mystack.pop()
                num1 = mystack.pop()
                num3 =0 
                if token == "+":
                    num3 = num1+num2
                elif token == '-':
                    num3 = num1-num2
                elif token == '*':
                    num3 = num1*num2
                else:
                    num3 = int(num1/num2)
                mystack.append(num3)
            else:
                mystack.append(int(token))
            
        return mystack[-1]

