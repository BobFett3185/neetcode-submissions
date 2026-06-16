class Solution:
    def climbStairs(self, n: int) -> int:
        # this is just recursive fibonacci sequence 
        # 1 stair = 1, 2 stairs =2, 3 stairs = 3, 4 stairs = 5  

        # basically we use caching here to store intermediate recursive calculations 
        cache = [-1] * (n+1)

        def fib(n):
            if n == 1 or n == 0:
                return 1
            
            if cache[n] != -1: # if we have the number just return it
                return cache[n]

            cache[n] = fib(n-1) + fib(n-2) # otherwise calculate it
            return cache[n]

        return fib(n)
        