class Solution:
    def rob(self, nums: List[int]) -> int:
        # at any point we can only rob from the maximum rob values of the last 2 elements
      
        rob1 =0
        rob2 =0

        for i in range(len(nums)):
            temp = max(rob1 + nums[i], rob2 )
            rob1 = rob2
            rob2 = temp
        
        return max(rob1, rob2)
            