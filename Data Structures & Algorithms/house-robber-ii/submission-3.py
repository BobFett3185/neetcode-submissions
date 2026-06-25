class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can turn this into 2 linear problems
        #one skips the first house, other skips the last house 
        if len(nums) ==1:
            return nums[0]
        def robHelper(nums): # same function from last problem
            rob1 =0
            rob2 =0 
            
            for i in range(len(nums)): # go through the list
                temp = max(nums[i]+rob1 , rob2) # rob house or stick with current
                rob1 = rob2  # move through
                rob2 = temp

            return max(rob1, rob2) 

        # return max of nums without first and max of nums without last
        return max(robHelper(nums[1:]), robHelper(nums[:-1]))
    