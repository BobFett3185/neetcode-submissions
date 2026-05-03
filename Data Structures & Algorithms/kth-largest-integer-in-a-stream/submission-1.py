
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        # we keep pushing onto heap and pop if the size exceeds k 
        #instance variables:
        self.minheap = [] # keep an array for our heap 
        self.k = k # keep k for use in the obj

        for i in range(len(nums)):
            heapq.heappush(self.minheap, nums[i])
            if len(self.minheap) > self.k:
                heapq.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        # if we exceed the height we need to pop
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
        # return smallest which is kth largest
        return self.minheap[0]
            
            


# we need to keep a min heap of size k 
# add a number to that min heap, then return min and restore 
# order. 

#useful functions:
#use heapq.heappush(heap, element) to push an element onto a heap
#use heapq.heappop(heap) to pop element