class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # you need to use 2 ptr to solve
        # basically find the max area and if the area is greater after moving reset max  

        # area = (end -start)* min(heights[end], heights[start])
        # only move the shorter line 
        start = 0 
        end = len(heights) -1 # set to last place in array 

        max =0
        while start < end :
            area = (end-start)* min(heights[end], heights[start])
            if area > max:
                max = area
            # move the shorter length rod
            if heights[end] > heights[start]: # if end is greater move start in 
                start += 1
            else:
                end -= 1  # otherwise move end left 
        return max 
            
        