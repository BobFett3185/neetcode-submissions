class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort() # gives us sorted by first number

        
        newIntervals =[intervals[0]] #we store our last merged interval in this 

        # basically the algo is to go through and compare our interval with the last merged one 
        for interval in intervals[1:]:
            if interval[0] <= newIntervals[-1][1]:# compare our interval start with end of last interval that was merged 
                newIn = [min(newIntervals[-1][0], interval[0]), max(newIntervals[-1][1], interval[1])]
                del newIntervals[-1]
                newIntervals.append(newIn)
            else:
                newIntervals.append(interval)

        return newIntervals



