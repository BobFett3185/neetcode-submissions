class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l =0 
        r=len(heights)-1
        maxArea =0 

        while(l<r):
            area = (r-l)*min(heights[l],heights[r]) # local area and update
            maxArea = max(area,maxArea)
            if heights[l]>heights[r]: # if left is bigger move right 
            # we do this because we want to keep the taller bar as a border 
                r-=1
            else:
                l+=1
        return maxArea
