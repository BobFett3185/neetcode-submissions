class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # another 2 ptr problem - can be done in o(n)
        # start and end should move together

        start =0
        end = 1
        maxProfit = 0 
        while end < len(prices): # move end until end of array 
            # profit when start is less than end 
            if prices[start] < prices[end]: # if the end price is higher calculate profit
                profit = prices[end]-prices[start]
                maxProfit = max(maxProfit, profit)
            else:
                start = end   # if end price is lower then move the new buy price to end 

            end+=1  # keep moving end to find potentially higher profit
        return maxProfit





        