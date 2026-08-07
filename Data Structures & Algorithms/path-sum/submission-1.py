# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # go down through tree passing a current value 
        # basically check if adding node to current gives you target 

        def dfs(node, currVal):
            if not node:
                return False
            if node.val + currVal == targetSum and not node.left and not node.right:
                return True 
            return dfs(node.left, node.val+currVal) or dfs(node.right, node.val+currVal)
        if dfs(root,0):
            return True
        else:
            return False
