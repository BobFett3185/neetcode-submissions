"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # should be pretty easy just sort by first number and then 
        intervals.sort(key=lambda x: x.start) # sort using a lambda func

        if not intervals: # edge case
            return True

        end = intervals[0].end # intialize end
        for interval in intervals[1:]: # for every next interval
            if interval.start < end: # check if its start clashes with last end 
                return False 
            end = interval.end # update end

        return True