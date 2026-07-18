class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # go through and if num -1 in array count
        map = {}
        # keys are the nums and the values are the length of the sequence with that

        # or just use a while loop to build sequence with a set for fast lookup 
        numbers= set(nums)
        result =0 
        for num in numbers:
            if num-1 not in numbers:
                count =0 
                curr = num
                while curr in numbers:
                    curr+=1
                    count+=1
                if count > result:
                    result = count 
        return result



