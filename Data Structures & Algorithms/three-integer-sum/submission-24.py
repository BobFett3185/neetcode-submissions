class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        print(nums)
        for index,num in enumerate(nums):
            l = index+1
            r = len(nums)-1

            # do finger search for other 2 numbers 
            if index> 0 and num == nums[index-1]:
                print("cont")
                continue
            
            while l < r:
                if nums[l]+nums[r]+num == 0 and index!=l and index!=r:
                    result.append([nums[l],nums[r],nums[index]])
                    l+=1
                    r-=1
                    while l<r and nums[l]== nums[l-1]:
                        l+=1
                    while l< r and nums[r] == nums[r+1]:
                        r-=1

                elif nums[l]+nums[r]+num > 0:
                    r-=1
                else:
                    l+=1
        return result
                
                    

            

        