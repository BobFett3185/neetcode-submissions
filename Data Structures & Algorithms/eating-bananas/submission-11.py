class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lowest =0 
        highest = max(piles) # O(n)
        # basically we do binary search to find min value between lowest and highest which works

        while lowest!=highest:#when these are equal we return
            k = (highest + lowest)//2 # find midpt
            if k ==0:
                return 1
            hours = 0
            for pile in piles: #find total hours required
                hours += math.ceil(pile/k)
            if hours>h: # if more than h we cant use this value
                lowest = k +1 
            else: # if higher than h then we can use this value
                highest = k

        return highest

        # doing binary search to half the search space each time. 