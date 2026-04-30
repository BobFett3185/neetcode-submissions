class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)-1

        # the key here is understanding the discrete cases 
        while l<=r:
            mid = (l+r) // 2 
            # if we find it
            if target == nums[mid]:
                return mid

            # in left sorted part
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
        return -1

            
            




 

    '''
        # some kind of binary search 

        l,r = 0, len(nums)-1
        while l < r:
            mid = (r -l+1)//2

            if target == nums[mid]:
                return mid
            if nums[l] <= target and target <= nums[mid]:
                l = mid + 1
            else :
                r = mid
            


        return -1


        '''