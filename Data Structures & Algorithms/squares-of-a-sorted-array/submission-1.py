class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        # go through and keep a left and right pointer and find whichever has greatest abs value
        l =0 
        r = len(nums)-1
        while l<=r: # go til pointer cross
            if abs(nums[l])> abs(nums[r]):
                result.append(nums[l]**2)
                l+=1
            else:
                result.append(nums[r]**2)
                r-=1
        result.reverse() # reverse result
        return result