class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # if interval comes before our current spot
                res.append(newInterval) # then we can append it and add rest of intervals and return
                return res+intervals[i:]
            elif newInterval[0] > intervals[i][1]: # if our interval comes after the current spot
                res.append(intervals[i]) # add current spot and move to next round 
            else: # we must have a merge so we need to change our new interval and then add it
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval) # if we changed this on the last one or if newInterval 
        #should go in the very last spot, then this is here
        # the other case returns immediately
        return res

