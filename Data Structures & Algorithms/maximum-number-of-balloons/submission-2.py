class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        for l in text:
            if l in letters:
                letters[l]+=1
            else:
                letters[l]=1
        for c in "balloon":
            if c not in letters:
                return 0
        
        # now go through and check 
        return min(letters['b'], letters['a'], letters['n'], letters['l']//2, letters['o']//2)
        '''
        count =0
        while True:
            if 'b' in letters:
                if letters['b'] ==1:
                    del letters['b']
                else:
                    letters['b']-=1
            else:
                break
            
            if 'a' in letters:
                if letters['a'] ==1:
                    del letters['a']
                else:
                    letters['a']-=1
            else:
                break

            if 'n' in letters:
                if letters['n'] ==1:
                    del letters['n']
                else:
                    letters['n']-=1
            else:
                break 

            if 'o' in letters and letters['o'] > 1:
                if letters['o'] < 3:
                    del letters['o']
                else:
                    letters['o']-=2
            else:
                break
            if 'l' in letters and letters['l'] > 1:
                if letters['l'] < 3:
                    del letters['l']
                else:
                    letters['l']-=2
            else:
                break  
            count+=1
        return count
        '''

