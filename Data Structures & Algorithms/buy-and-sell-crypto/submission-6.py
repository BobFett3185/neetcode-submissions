class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # another 2 ptr problem - can be done in o(n)
        # start and end should move together

        start =0
        end = 1
        maxProfit = 0 
        while end < len(prices):
            # profit when start is less than end 
            if prices[start] < prices[end]:
                profit = prices[end]-prices[start]
                maxProfit = max(maxProfit, profit)
            else:
                start = end

            end+=1 
        return maxProfit





        