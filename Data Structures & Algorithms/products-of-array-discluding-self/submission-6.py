class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # create 2 arrays which store the multiplied values to the left and right of their index 
        left = [1]*len(nums)
        right = [1]*len(nums) 
        leftM = 1 
        rightM = 1 
        for i in range(1,len(nums)):
            left[i] = leftM*nums[i-1]
            leftM = left[i]
        for j in range(len(nums)-2,-1,-1):
            right[j] = rightM*nums[j+1]
            rightM = right[j]
        
        result =[]
        for k in range(len(nums)):
            result.append(left[k]*right[k])
        return result
        
        # 1  2 4 6
        # 1  1 2 8 left 
        #48 24 6 1