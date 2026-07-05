class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # basically we sort them, and if there is overlap we delete the one with a bigger end value
        # then move your end to the minimum if there was a merge and move it to end if no merge 
        intervals.sort()
        count =0
        end = intervals[0][1]
        # compare pairs and if you need to delete then increment count
        for interval in intervals[1:]:
            if interval[0] < end: # if the start of interval is before the end of last interval 
                count+=1  # then increment count 
                end = min(end,interval[1]) # do this bc it leaves more room for future intervals
            else:
                end = interval[1] # otherwise just update end
        return count
            
            

        