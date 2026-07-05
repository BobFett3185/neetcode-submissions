class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # basically we sort them, and if there is overlap we delete the one with a bigger end value
        intervals.sort()
        count =0
        end = intervals[0][1]
        # compare pairs and if you need to delete then increment count
        for interval in intervals[1:]:
            if interval[0] < end: # if the start of interval is before the end of last interval 
                count+=1 
                end = min(end,interval[1])
            else:
                end = interval[1]
        return count
            
            

        