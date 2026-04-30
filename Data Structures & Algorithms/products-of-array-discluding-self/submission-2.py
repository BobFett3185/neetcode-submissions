class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # just multiply by all then divide by what's excluded 
        length = len(nums)
        output = [0] * length

        product =1
         
        if nums == [0] * length:
            return nums


        for num in nums: # get product of whole array
            product *= num

        countZero =0; 
        
        product2 = 1
        for num in nums:
            if num != 0:
                product2 *= num
            else:
                countZero += 1 
        
        if countZero > 1:
            output = [0] * length
            return output


        for i in range(length):
            if nums[i] == 0:
                output[i] = product2
            else:
                output[i] = int(product/nums[i])
        return output

        

        