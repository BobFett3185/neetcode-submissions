class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # basically work from the end and keep shifing our goalpost towards the front 
        # start at end and look if the one in front can reach it, if it does 
        # then we can move our end goalpost to there -- bc we know we can get from there to last index

        # greedy solution working from the back 
        goal = len(nums) -1
        for i in range(len(nums)-2, -1, -1): # go from end to front 
            if nums[i] + i >= goal:
                goal = i

        if goal ==0: # if we made it back to the front
            return True 
        return False