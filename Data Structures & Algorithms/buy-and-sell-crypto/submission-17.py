class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use 2 ptr 
        # move left after calcualting a profit 


        profit =0 
        l =0
        r = 1

        # move them together
        while r<len(prices):
            if prices[r] < prices[l]:
                l = r 
            else:
                profit = max(profit, prices[r]-prices[l])
            r+=1 
        return profit

