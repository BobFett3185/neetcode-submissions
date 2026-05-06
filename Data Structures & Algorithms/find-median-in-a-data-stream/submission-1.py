class MedianFinder:

    def __init__(self):
        self.lh = []
        self.rh = []        

    def addNum(self, num: int) -> None:
        if len(self.lh) == len(self.rh):
            # maintain ordering with rh
            if self.rh and num > self.rh[0]:
                heapq.heappush(self.lh, -heapq.heappop(self.rh))
                heapq.heappush(self.rh, num)
            else:
                heapq.heappush(self.lh, -num)

        elif len(self.rh) > len(self.lh):
            if num > self.rh[0]:
                heapq.heappush(self.lh, -1*(heapq.heappop(self.rh)))
                heapq.heappush(self.rh, num)
            else:
                heapq.heappush(self.lh, -1*num)
        else: # lh is bigger 
            if num < -1*(self.lh[0]):
                heapq.heappush(self.rh, -1*(heapq.heappop(self.lh)))
                heapq.heappush(self.lh,-1*num)
            else:
                heapq.heappush(self.rh, num)
        

    def findMedian(self) -> float:
        if len(self.rh) == len(self.lh):
            return (self.rh[0] + -1*(self.lh[0]))/2
        elif len(self.rh)>len(self.lh):
            return self.rh[0]
        else:
            return -1*self.lh[0]
        
'''
partition into a min heap for right side of array and a max heap for left side of array
this way we can see the middlemost values 

keep them seperated by the current median as you build the heaps
they should be same size or 1 off

adding:
if heaps are same size:
    push to leftside and update median to be the max of that heap -- O(1)
if right heap is bigger 
    if greater than min of right side, 
        move min of rightside to leftside 
        push to rightside
    else   
        put in left side

if left side is bigger
    if less than max of left side
        move nax to right side 
        push to left side 
    else 
        put in right side


find median:
if equal size, compare the 2 popped elements

if not, whichever is bigger stores the median in its pop




    '''