class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)-1

        # the key here is understanding the discrete cases 
        while l<=r:# binary search condition
            mid = (l+r) // 2  # find our mid

            if target == nums[mid]: # if we find return
                return mid

            # if the left part is the sorted part 
            if nums[l] <= nums[mid]:
                #check if the target doesn't fit in this sorted part
                if target > nums[mid] or target < nums[l]:  # if it doesnt fit in left part then we 
                    l = mid +1
                else:
                    r = mid -1

            # if the right part is sorted
            else:
                #check if the target doesn't fit in this sorted part
                if target < nums[mid] or target > nums[r]:
                    r = mid -1 # if it doesnt fit in the right part we can move right ptr
                else:
                    l = mid + 1 # if it does fit, then we can move our left pointer
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