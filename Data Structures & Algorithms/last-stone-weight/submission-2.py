class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # just implement a min heap with negative values for a max heap here
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, (0-stone))
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x == y:
                continue 
            else:
                heapq.heappush(maxHeap, (0-abs(x-y)))
        
        if len(maxHeap) ==0:
            return 0
        return maxHeap[0]*-1


        '''
        psuedocode
        make a max heap to keep track of big stones
        push eveythign onto it 




































$0
        then pop elemnt 1 and store 
        pop elemrnt 2and store 
        keep going until len of heap is 1 and then return 
        '''

        # useful functions
        #use heapq.heappush(heap, element) to push an element onto a heap
        #use heapq.heappop(heap) to pop element 
        