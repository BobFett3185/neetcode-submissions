class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we are looking for a contiguous substring 
        # go through and keep track of seen elements in a set 

        seen = set()

        # use 2 pointer approach to keep track of left and right bounds of a substring 
        # check if next element in the set, if it is remove the elemnt at left, then increment left and check again 
        left = 0
        result =0 

        for index, num in enumerate(s):
            while num in seen:
                seen.remove(s[left])
                left+=1 
            seen.add(num)
            result = max(result, index - left+1)
        return result