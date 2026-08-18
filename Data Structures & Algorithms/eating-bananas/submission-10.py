class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lowest =0 
        highest = max(piles) # O(n)

        while lowest!=highest:#what should this be???
            k = (highest + lowest)//2
            if k ==0:
                return 1
            hours =0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours>h:
                lowest = k +1 
            else:
                highest = k
        return highest
            






        




        return k