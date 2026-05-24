class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] 
        # i keeps track of which numbers we can choose from
        # curr is a current list of what we have added
        # running total = total 
        def dfs(i, curr, total):
            
            # base cases: 
            if total == target:
                result.append(curr.copy())#add a copy so you can still work with curr
                return 
            if i>= len(nums) or total > target: #if at end of list or total has gone over
                return 
            
            curr.append(nums[i])
            dfs(i, curr, total+nums[i])
            
            curr.pop() # can no longer use that element
            dfs(i+1, curr, total) # call dfs

        dfs(0,[],0)
        return result
        
        #go through and find the possible tracks then 
        #basically a dfs with backtracking, we need to sort nums to ensure early stopping 

