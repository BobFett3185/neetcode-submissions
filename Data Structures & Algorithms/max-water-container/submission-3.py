class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers starting from opposite end 
        result =0 
        l,r = 0, len(heights)-1

        while l<r:
            result = max(result, (r-l)*min(heights[r],heights[l]))
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1 
        return result
            