# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]#keep this for global storage 
        # returns the max path without a split 
        def dfs(root):
            # base case
            if not root:
                return 0
            
            #crawl down the tree
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            #only consider positive value
            leftMax = max(leftMax,0)
            rightMax = max(rightMax,0)

            # now compute max path with a split
            #basically checking if this is a better place to split at
            # as we crawl back up we keep updating result
            result[0] = max(result[0], leftMax+rightMax+root.val)
            return root.val+ max(leftMax, rightMax)

        dfs(root)#call function and return
        return result[0]

