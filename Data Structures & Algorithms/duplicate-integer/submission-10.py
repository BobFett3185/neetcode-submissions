class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # basically add to set and if alr in set return false 

        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False 