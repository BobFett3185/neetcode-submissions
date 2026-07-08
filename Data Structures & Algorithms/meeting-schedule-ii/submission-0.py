"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we can keep track of occurences with a hash map 
        # when we hit a start time increment, end decrement 
        # when we finish go through and add to a running andd check if running > max 

        result =0
        mymap = {}
        for interval in intervals:
            if interval.start not in mymap:
                mymap[interval.start] = 1
            else:
                mymap[interval.start]+=1 

            if interval.end not in mymap:
                mymap[interval.end] = -1
            else:
                mymap[interval.end]-=1 
        curr =0
        sort = dict(sorted(mymap.items()))
    
        for time in sort:
            curr+=sort[time]
            if curr > result:
                result = curr
                

        return result


