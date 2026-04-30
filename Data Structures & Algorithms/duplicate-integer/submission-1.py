class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((nums[i]+nums[j])/ 2 == nums[i]) and (i != j):
                    return True

        return False
         