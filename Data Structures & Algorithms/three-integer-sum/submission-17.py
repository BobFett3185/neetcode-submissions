class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # need to sort then use 2 ptr to try and find other 2 nums 

        nums = sorted(nums)
        result = []
        
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    result.append([nums[i],nums[l],nums[r]])

                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]== nums[r+1]:
                        r-=1
                    
                elif total>0:
                    r-=1
                else:
                    l+=1
        return result
    