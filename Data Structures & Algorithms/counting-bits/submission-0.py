class Solution:
    def countBits(self, n: int) -> List[int]:
        # we can keep track of the previous work in a similar way and express each value as 
        # 1+ dp[i-offset]
        # we update the offset everytime we get to an index 2*offset  -> set offset to index
        dp =[0]*(n+1)
        offset =1 
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1+dp[i-offset]
        return dp

