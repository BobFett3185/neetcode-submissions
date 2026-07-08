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
            if interval.start not in mymap: # if start not there just make it 1
                mymap[interval.start] = 1
            else:
                mymap[interval.start]+=1  # else add 1 to it

            if interval.end not in mymap: # if end not there make it -1
                mymap[interval.end] = -1
            else:
                mymap[interval.end]-=1  # if its there just decrement

        curr =0
        sort = dict(sorted(mymap.items()))# sort this so we go in order time wise
    
        for time in sort:
            curr+=sort[time] # keep a running total 
            if curr > result: # if it crosses max then update result
                result = curr

        return result


