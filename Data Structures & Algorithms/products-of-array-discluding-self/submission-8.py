class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # cache intermediate results

        leftMult = [1]
        rightMult = []

        left =1
        right =1

        for num in nums[:len(nums)-1]:
            left*=num
            leftMult.append(left)
        for i in range(len(nums)-1, 0, -1):
            right*=nums[i]
            rightMult.append(right)
        
        rightMult=rightMult[::-1]
        rightMult.append(1)



        # now you multiply 2 things 
        result = []
        for i in range(len(nums)):
            result.append(leftMult[i]*rightMult[i])
        return result
        